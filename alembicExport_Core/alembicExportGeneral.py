import maya.cmds as cmds
import maya.mel as mel

class AlembicUtils():

	@staticmethod
	def loadAbcPlugin():
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

	@staticmethod
	def startEnd():
		start = int(cmds.playbackOptions(q=True, min=True))
		end = int(cmds.playbackOptions(q=True, max=True))

		return start, end
	
	@staticmethod
	def path():
		path_ = cmds.fileDialog2(fm=3, dialogStyle=2, cc='Cancel')
		if path_:
			return path_[0] + '/'

class alembicExportGral:
	def __init__(self):
		
		self.refs = []
		self.listType = []

	def main(self, ref, start, end, path, fileName):


		geo = self.findGeo(ref)
		root = self.getAlembicRoot(geo)
		self.exportAbc(geo, root, path, fileName, start, end) 

	def getNamespace(self, ref):
		'''
		'''
		namespace = cmds.file(ref, q=True, ns=True)
		return namespace
	
	def setNamespace(self, ref, newNamespace):
		'''
		'''
		return cmds.file(ref, e=True, ns=newNamespace)

	def getNameObj(self, obj):
		'''
		get name of obj, split if it comes from a ref
		'''
		if cam.find(':') != -1:
			return cam.split(':')[-1]
		else:
			return cam

	def findRefs(self):
		'''
		queries all reference paths
		'''
		refs = (cmds.file(q=True, r=True))
		return refs

	def exportAbc(self, geo, root, path, abcFile, start, end):
		'''
		Deals with alembic export
		'''
		cmds.select(geo)
		cmds.refresh()
		command = '"-frameRange ' + str(start) + " " + str(end) + ' -sl -uvWrite -dataFormat ogawa -root ' + str(root) + ' -file \\"' + str(path) + str(abcFile) +'.abc\\"\"'
		
		mel.eval('AbcExport -j ' + str(command))

	def clearSel(self):

		cmds.select(cl=True)

	def selectObj(self, obj):

		cmds.select(obj)

	def selectShape(self, obj):
		print obj
		shape = cmds.listRelatives(obj, s=True, f=True)[0]
		return shape

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

class alembicExportGeo(alembicExportGral):

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
				refList.append(shapes[0])
		return refList

	def selectGeoFromRef(self, ref):
		geo = self.findGeo(ref)
		cmds.select(geo)

	def getAlembicRoot(self, geometry):
		'''
		Gets the common parent for all geometry 
		'''
		root = ''
		for geo in geometry:
			if root != '':
				geoSplitted = geo.split('|')
				rootSplitted = root.split('|')

				if len(geoSplitted) > len(rootSplitted):
					root = self.getParent(geoSplitted, rootSplitted)
				else:
					root =self.getParent(rootSplitted, geoSplitted)
			else:
				root = geo

		return root

	def getParent(self, lengthyList, shortyList):
		'''
		getAlembicRoot submethod
		'''
		root = []

		for geo in lengthyList:
			if geo in shortyList:
				root.append(geo)

		root = '|'.join(root)
		return root

class alembicExportCams(alembicExportGral):

	def main(self, cam, start, end, path, fileName):
		
		camShape = self.selectShape(cam)
		self.exportAbc(camShape, cam, path, fileName, start, end) 

	def findCams(self):
		'''
		query all referenced and non-referenced cams
		'''
		invalidCameras = ['frontShape', 'sideShape', 'topShape', 'perspShape']
		cameras = [cmds.listRelatives(cam, p=True)[0] for cam in cmds.ls(et='camera') if cam not in invalidCameras]
		return cameras

	def getNameCam(self, cam):

		if cam.find(':') != -1:
			return cam.split(':')[-1]
		else:
			return cam

