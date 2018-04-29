from Modules.Qt import QtCore, QtGui, QtWidgets
import Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExport
reload(Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExport)
from Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExport import *#import alembicExport
from functools import partial
import getpass


import Utils.Slack_sendMessage.MKF_SlackMessages
reload(Utils.Slack_sendMessage.MKF_SlackMessages)
from Utils.Slack_sendMessage.MKF_SlackMessages import Slack


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

		self.font = QtGui.QFont()
		self.font.setBold(True)
		self.font.setPointSize(9)

		#self.window.resize(600, 300)

		self.reg_ex = QtCore.QRegExp("[a-zA-Z0-9_]+")

		#self.window.setFixedSize(500, 300)
		self.lineEdits = []
		self.checkBoxes = []
		self.checkBoxesCam = []
		self.refs = []
		self.path = os.getenv("HOME")
		self.user = getpass.getuser()
		self.core = alembicExport()
		self.core.loadAbcPlugin()
		self.populateUI()

		self.slack = Slack()


	def populateUI(self):

		'''
		Finds all references, creates them a checkbox and a lineEdit, sets the lineEdit's text 
		to the nameSpace found
		'''
		self.readLocalInfo(self.path + '/abcPath.txt', self.txt_path)

		#finds alembics in refs and cams in all the scene
		self.refs = self.findRefs()
		self.cams = self.findCams()

		startEnd = self.startEnd()
		self.txt_startFrame.setText(str(startEnd[0]))
		self.txt_endFrame.setText(str(startEnd[1]))
		grid = 0

		#block for refs of geo
		if len(self.refs) > 0:
			for ref in self.refs:
				#referenced files
				grid += 1
				nameSpace = self.core.getNamespace(ref)
				checkBox = QtWidgets.QCheckBox('')
				self.lyt_grid_references.addWidget(checkBox, grid, 0, 1, 1)
				self.checkBoxes.append(checkBox)
				txt_name = QtWidgets.QLineEdit(nameSpace)
				self.lineEdits.append(txt_name)
				self.lyt_grid_references.addWidget(txt_name, grid, 1, 1, 1)

				#validator = QtGui.QRegExpValidator(self.reg_ex, txt_name)
				#txt_name.setValidator(validator)

		text_cams = QtWidgets.QLabel('Available cameras to export')
		self.lyt_grid_references.addWidget(text_cams, grid + 1, 1, 1, 1)
		text_cams.setFont(self.font)
		grid += 1

		#block for cams
		if len(self.cams) > 0:
			for cam in self.cams:
				#cams
				grid += 1
				#nameOrNameSpace = self.core.getNameCam(ref)
				nameOrNameSpace = self.core.getNameCam(cam)
				checkBox = QtWidgets.QCheckBox('')
				self.lyt_grid_references.addWidget(checkBox, grid, 0, 1, 1)
				self.checkBoxesCam.append(checkBox)
				txt_nameOrNameSpace = QtWidgets.QLineEdit(nameOrNameSpace)
				self.lineEdits.append(txt_nameOrNameSpace)
				self.lyt_grid_references.addWidget(txt_nameOrNameSpace, grid, 1, 1, 1)

				validator = QtGui.QRegExpValidator(self.reg_ex, txt_nameOrNameSpace)
				txt_nameOrNameSpace.setValidator(validator)

			text_cams = QtWidgets.QLabel('\n No es necesario seleccionar nada, solo marcar la casilla \n')
			self.lyt_grid_references.addWidget(text_cams, grid + 1, 1, 1, 1)


		for num in range(0, len(self.checkBoxes)):
			'''
			signals can't be connected through a for loop, 
			lambda avoids overriding in each iteration
			'''
			self.checkBoxes[num].stateChanged.connect(lambda state, n=num: self.testSignal(n))


	def findRefs(self):
		self.refs = self.core.findRefs()
		return self.refs

	def findCams(self):
		self.cams = self.core.findCams()
		return self.cams

	def startEnd(self):
		startEnd = self.core.startEnd()
		return startEnd

	def exportAlembic(self):

		checkedRefs = ''

		start = str(self.txt_startFrame.text())
		end = str(self.txt_endFrame.text())
		path = self.txt_path.text()


		if path.find('Z:/') == -1 or path.find('//master') == -1: 
			self.writeLocalInfo(self.path + '/abcPath.txt', self.txt_path.text())


		for x in range(0, len(self.checkBoxes)):
			if self.checkBoxes[x].isChecked() == True:
				self.core.changeNamespace(self.refs[x], self.lineEdits[x].text())
				self.core.main(self.refs[x], start, end, path)

				checkedRefs += self.lineEdits[x].text() + ', '

		if checkedRefs != '':
			try:
				self.slack.MessageSlack(Message = 'Alembics *' + checkedRefs + '* guardado en la ruta: *' + path + '* del usuario `' + self.user + '`', channel = 'rnd')
			except:
				pass

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

