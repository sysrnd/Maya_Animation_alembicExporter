import maya.cmds as cmds
import maya.mel as mel
import os

FILE = cmds.file(q=True, sn=True).strip(cmds.file(q=True, sn=True).split('/')[-1])
class alembicExport(object):
	def __init__(self):
		self.refs = []

	def main(self, ref, start, end, path):

		abcDir = path + '/'
		geo = self.findGeo(ref)
		root = self.parseRootString(geo)
		fileName = self.alembicName(ref, geo[0])
		self.exportAbc(root, abcDir, fileName, start, end) 

	def getFile():

		return FILE


	def alembicName(self, ref, geo):
		fileName = geo.split('|')[-1].rpartition(':')[0]
		fileName += '_'
		fileName += cmds.file(q=True, sn=True).split('/')[-1].split('.')[-2]
		#fileName = fileName.strip('RG_')
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
	def findRefs(self):
		'''
		querys all reference paths
		'''

		refs = (cmds.file(q=True, r=True))
		return refs

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
				if len(shapes) < 1:
					validgeo = False
			else:
				validgeo = False


			for nogeo in ignoreGeoList:
				if geo.find(nogeo) != -1:
					validgeo = False

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
		command = '"-frameRange ' + str(start) + " " + str(end) + ' -dataFormat ogawa ' + str(root) + '-file \\"' + str(path) + str(abcFile) +'.abc\\"\"'
		print command
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