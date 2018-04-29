from PyQt4 import QtCore, QtGui


import Animacion.Maya_animation_AlembicExporter.alembicExport_Core.alembicExport
reload(Animacion.Maya_animation_AlembicExporter.alembicExport_Core.alembicExport)
from Animacion.Maya_animation_AlembicExporter.alembicExport_Core.alembicExport import *#import alembicExport

from functools import partial

class alembicExportBridge(object):

	def __init__(self, window):
		'''

		'''
		self.window = window
		self.lyt_main = window.lyt_main
		self.lyt_grid_references = window.lyt_grid_references
		self.txt_startFrame = window.txt_startFrame
		self.txt_endFrame = window.txt_endFrame
		self.txt_path = window.txt_path
		self.lbl_status = window.lbl_status
		self.btn_exportAlembic = window.btn_exportAlembic
		self.btn_exportAlembic.clicked.connect(self.exportAlembic)
		self.btn_path = window.btn_path
		self.btn_path.clicked.connect(self.getPath)

		#self.window.resize(600, 300)
		#self.window.setFixedSize(500, 300)
		self.lineEdits = []
		self.checkBoxes = []	
		self.refs = []
		self.path = os.getenv("HOME")

		self.core = alembicExport()
		self.core.loadAbcPlugin()
		self.populateUI()

	def populateUI(self):
		'''

		'''
		self.readLocalInfo(self.path + '/abcPath.txt', self.txt_path)

		self.refs = self.findRefs()
		startEnd = self.startEnd()

		grid = 0
		self.signals = []


		if len(self.refs) > 0:
			for ref in self.refs:
				grid += 1
				nameSpace = self.core.getNamespace(ref)
				checkBox = QtGui.QCheckBox('')
				self.lyt_grid_references.addWidget(checkBox, grid, 0, 1, 1)
				self.checkBoxes.append(checkBox)
				txt_nameSpace = QtGui.QLineEdit(nameSpace)
				self.lineEdits.append(txt_nameSpace)
				self.lyt_grid_references.addWidget(txt_nameSpace, grid, 1, 1, 1)
				#signal = checkBox.stateChanged.connect(self.testSignal)
		self.txt_startFrame.setText(str(startEnd[0]))
		self.txt_endFrame.setText(str(startEnd[1]))
		for num in range(0, len(self.checkBoxes)):
		#for checkbox in self.checkBoxes:
			self.checkBoxes[num].stateChanged.connect(lambda state, n=num: self.testSignal(n))

	def findRefs(self):
		self.refs = self.core.findRefs()
		return self.refs

	def startEnd(self):
		startEnd = self.core.startEnd()
		return startEnd

	def exportAlembic(self):
		start = str(self.txt_startFrame.text())
		end = str(self.txt_endFrame.text())

		path = self.txt_path.text()

		if path.find('Z:/') == -1 or path.find('//master') == -1: 
			self.writeLocalInfo(self.path + '/abcPath.txt', self.txt_path.text())

		for x in range(0, len(self.checkBoxes)):
			if self.checkBoxes[x].isChecked() == True:
				self.core.changeNamespace(self.refs[x], self.lineEdits[x].text())
				self.core.main(self.refs[x], start, end, path)

	def getPath(self):
		path = self.core.path()
		self.txt_path.setText(path)

	def testSignal(self, num):
		state = self.checkBoxes[num].isChecked()

		if state == True:
			self.core.selectGeoFromRef(self.refs[num])
		else:
			self.core.clearSel()

	def readLocalInfo(self, file, txt):
		if os.path.exists(file + '.txt'):
			with open(file + '.txt' ,'r') as f:
				data = f.read()
			txt.setText(data)
			return True
		else:
			return False

	def writeLocalInfo(self, file, txt):
		with open(file + '.txt','w') as f:
			data = f.write(txt)
