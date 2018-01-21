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

	def dirAlembic(self, sceneDir=FILE, taskFolderString = 'ANIMACION'):
		'''
		Checks if folder "ALEMBICS" exist, if it doesn't creates a new one
		'''

		if taskFolderString not in sceneDir:
			cmds.warning( 'La carpeta \"' + str(taskFolderString) + '\" no fue encontrada' )
		else:
			if not os.path.exists(sceneDir + 'ALEMBICS'):
				abcDir = os.mkdir(sceneDir + 'ALEMBICS')
				#cmds.warning("La carpeta \"ALEMBICS\" no existia y fue creada")
			else:
				#print "Se encontro la carpeta \"ALEMBICS\"",
				abcDir = sceneDir + 'ALEMBICS/'

			return abcDir
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

		for geo in cmds.referenceQuery(ref, dp=True, nodes=True):
			if cmds.objectType(geo) == 'mesh':
				
				validgeo = True

				for nogeo in ignoreGeoList:
					if geo.find(nogeo) != -1:
						validgeo = False

				transform = cmds.listRelatives(geo, parent=True, f=True)[0]
				transformVis = cmds.getAttr(transform + '.visibility')

				if transformVis == False:
					validgeo = False
				try:
					parent = cmds.listRelatives(transform, parent=True, f=True)[0]
					parentVis = cmds.getAttr(parent + '.visibility')
					if parentVis == False:
						validgeo = False
				except:
					pass

				shapes = cmds.listRelatives(transform, s=True)

				if validgeo == True:
					if len(shapes) > 1:
						refList.append(transform)

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
		command = '"-frameRange ' + str(start) + " " + str(end) + ' -dataFormat ogawa' + str(root) + '-file \\"' + str(path) + str(abcFile) +'.abc\\"\"'
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
		print 'testiriiririr'
		'''
		geo = []
		cmds.file(ref, sa=True)
		sel = cmds.ls(sl=True, l=True)
		cmds.select(cl=True)
		for x in sel:
			if cmds.objectType(x) == 'mesh':
				if x.find('BS_') == -1:
					if x.find('BORRAR') == -1:
						if x.find('WRAP') == -1:
							xParent = cmds.listRelatives(x, p=True, f=True)[0]
							geo.append(xParent)

		cmds.select(geo)
		'''

	def clearSel(self):
		cmds.select(cl=True)