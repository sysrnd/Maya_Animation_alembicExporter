import maya.cmds as cmds
import maya.mel as mel
import os

FILE = cmds.file(q=True, sn=True).strip(cmds.file(q=True, sn=True).split('/')[-1])
class alembicExport(object):
	def __init__(self):
		self.refs = []

		self.listType = []

	def main(self, ref, start, end, path):

		abcDir = path + '/'
		geo = self.findGeo(ref)
		root = self.parseRootString(geo)
		fileName = self.alembicName(ref, geo[0])
		self.exportAbc(root, abcDir, fileName, start, end) 

	def getFile():

		return FILE


	def alembicName(self, ref, geo):
		'''
		name of the alembic file
		deprecated
		'''
		fileName = cmds.file(ref, q=True, ns=True)
		return fileName

	def getNamespace(self, ref):
		'''
		'''
		namespace = cmds.file(ref, q=True, ns=True)
		return namespace
	
	def setNamespace(self, ref, newNamespace):
		'''
		'''
		return cmds.file(ref, e=True, ns=newNamespace)

	def getNameCam(self, cam):

		if cam.find(':') != -1:
			return cam.split(':')[-1]
		else:
			return cam

	def setNameCam(self, cam, newName):
		if cam.find(':') != -1:
			return cam.split(':')[-1]
		else:
			cmds.rename(cam, newName)

	def findRefs(self):
		'''
		querys all reference paths
		'''
		refs = (cmds.file(q=True, r=True))
		return refs

	def findCams(self):
		'''
		query all referenced and non-referenced cams
		'''
		invalidCameras = ['frontShape', 'sideShape', 'topShape', 'perspShape']
		cameras = [cmds.listRelatives(cam, p=True)[0] for cam in cmds.ls(et='camera') if cam not in invalidCameras]
		return cameras


	def changeNamespace(self, ref, newNs):
		'''
		'''

		newNamespace = cmds.file(ref, e=True, ns=newNs)
		return newNamespace

	def findGeo(self, ref):
		'''
		Finds all 'valid' geo from reference

		Ignores blendshapes, wraps and wires by checking if it finds them from a list
		'''
		ignoreGeoList = ['BS', 'WRAP', 'BORRAR', 'Base']
		refList = []

		for geo in cmds.referenceQuery(ref, dp=True, nodes=True, sdp=True):
			
			validgeo = True
			
			shapes = cmds.listRelatives(geo, s=True, f=True)
			if shapes != None:
				if cmds.objectType(shapes[0]) != 'mesh':
					validgeo = False
				else:
					#check for visibility 
					if self.checkVis_Recursive(geo) == False:
						validgeo = False

				#check to OrigShape existance
				if len(shapes) < 1:
					validgeo = False
			else:
				validgeo = False

			#scan for invalid geo list
			for nogeo in ignoreGeoList:
				if geo.find(nogeo) != -1:
					validgeo = False



			#end validation process, appends to list
			if validgeo == True:
					parent = cmds.listRelatives(shapes[0], p=True, f=True)[0]
					refList.append(parent)

		return refList

	def loadAbcPlugin(self):
		'''
		Checks if plugin AbcExport is loaded to avoid any errors
		'''
		try:
			if 'AbcExport' in cmds.pluginInfo(query=True, listPlugins=True):
				pass
			else:
				cmds.loadPlugin("AbcExport")
				cmds.warning( "El plugin \"AbcExport\" no estaba cargado, intenta de nuevo" )
		except:
			pass

	def startEnd(self):
		start = int(cmds.playbackOptions(q=True, min=True))
		end = int(cmds.playbackOptions(q=True, max=True))

		return start, end
	def exportAbc(self, root, path, abcFile, start, end):
		'''
		Deals with alembic export
		'''
		command = '"-frameRange ' + str(start) + " " + str(end) + ' -uvWrite -dataFormat ogawa ' + str(root) + '-file \\"' + str(path) + str(abcFile) +'.abc\\"\"'
		mel.eval('AbcExport -j' + str(command))

	def parseRootString(self, geo):
		'''

		'''
		root = ''

		for x in geo:
			root += '-root ' + str(x) + ' '

		return root
		
	def path(self):
		path_ = cmds.fileDialog2(fm=3, dialogStyle=2, cc='Cancel')
		if path_:
			return path_[0]

	def selectGeoFromRef(self, ref):
		geo = self.findGeo(ref)
		cmds.select(geo)


	def clearSel(self):
		cmds.select(cl=True)

	def checkVis_Recursive(self, obj):
		'''
		do it recurvively
		'''
		objParent = cmds.listRelatives(obj, p=True, f=True)
		
		if type(objParent) == type(self.listType):
			if objParent[0] != None:
				vis = cmds.getAttr(objParent[0] + '.visibility')
				if vis == False:
					return vis
				else:
					self.checkVis_Recursive(objParent)