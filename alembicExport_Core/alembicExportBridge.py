#TODO: UPDATE STATUS BAR EXPORTED
#GENERAL CLASS OPT
#DEAL WITH MAIN IN CORE
#FIX CHECKVISRECURSIVE AND SELF.LISTTYPE
#FIX UI NAMES LAYOUT, ADD SELECTED TAB

import Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExportGeneral 
reload(Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExportGeneral)
from Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExportGeneral import *
from Modules.Qt import QtCore, QtGui, QtWidgets
from functools import partial
import getpass
import os


import Utils.Slack_sendMessage.MKF_SlackMessages
reload(Utils.Slack_sendMessage.MKF_SlackMessages)
from Utils.Slack_sendMessage.MKF_SlackMessages import Slack


class alembicExportBridge(object):
	def __init__(self, window):

		'''
		initial config with static methods, yay!
		'''
		AlembicUtils().loadAbcPlugin()
		self.activeRefs = 0
		self.path = os.getenv("HOME") + '/'
		self.startEnd = AlembicUtils.startEnd()

		self.window = window
		self.window.btn_exportAlembic.clicked.connect(self.exportAlembic)
		self.window.btn_path.clicked.connect(self.getPath)

		self.reg_ex = QtCore.QRegExp("[a-zA-Z0-9_]+")

		self.lineEdits = []
		self.lineEditsCam = []
		self.checkBoxes = []
		self.checkBoxesCam = []

		self.core = alembicExportGral()
		self.geo = alembicExportGeo()
		self.cam = alembicExportCams()

		self.initialInfo()
		self.populateUI()

	def initialInfo(self):

		self.window.txt_startFrame.setText(str(self.startEnd[0]))
		self.window.txt_endFrame.setText(str(self.startEnd[1]))
		
		self.readLocalInfo(self.path + '/abcPath', self.window.txt_path)

		self.refs = self.geo.findRefs()
		self.cams = self.cam.findCams()


	def populateUI(self):
		'''
		Finds all references, creates them a checkbox and a lineEdit, sets the lineEdit's text 
		to the nameSpace found
		'''

		grid = 0

		#block for refs of geo
		if len(self.refs) > 0:
			for ref in self.refs:
				#referenced files
				grid += 1
				nameSpace = self.geo.getNamespace(ref)
				self.createValidCheckbox(grid, nameSpace, self.window.lyt_vertical_geo, self.checkBoxes, self.lineEdits)

		grid = 0

		if len(self.cams) > 0:
			for cam in self.cams:
				#cams
				grid += 1
				#nameOrNameSpace = self.core.getNameCam(ref)
				nameOrNameSpace = self.cam.getNameCam(cam)
				self.createValidCheckbox(grid, nameOrNameSpace, self.window.verticalLayout, self.checkBoxesCam, self.lineEditsCam)

		for num in range(0, len(self.checkBoxes)):
			'''
			signals can't be connected through a for loop, 
			lambda avoids overriding in each iteration
			'''
			self.checkBoxes[num].stateChanged.connect(lambda state, n=num: self.geoSelectSignal(n))

		for num in range(0, len(self.checkBoxesCam)):

			self.checkBoxesCam[num].stateChanged.connect(lambda state, n=num: self.camSelectSignal(n))

	def createValidCheckbox(self, num, name, layout, listCB, listLE):
		checkBox = QtWidgets.QCheckBox('')
		layout.addWidget(checkBox, num, 0, 1, 1)
		listCB.append(checkBox)
		txt_name = QtWidgets.QLineEdit(name)
		listLE.append(txt_name)
		layout.addWidget(txt_name, num, 1, 1, 1)
		validator = QtGui.QRegExpValidator(self.reg_ex, txt_name)
		txt_name.setValidator(validator)

	def exportAlembic(self):
		'''
		'''

		#for slack purposes
		checkedRefs = ''

		start = str(self.window.txt_startFrame.text())
		end = str(self.window.txt_endFrame.text())
		path = self.window.txt_path.text()

		self.writeLocalInfo(self.path + 'abcPath', self.window.txt_path.text())


		avCheckBoxes = self.checkBoxes + self.checkBoxesCam

		for x in xrange(0, len(self.checkBoxes)):
			if self.checkBoxes[x].isChecked() == True:
				self.geo.setNamespace(self.refs[x], self.lineEdits[x].text())
				self.geo.main(self.refs[x], start, end, path, self.lineEdits[x].text())
				checkedRefs += self.lineEdits[x].text() + ', '

		self.cams = self.cam.findCams()

		for y in xrange(0, len(self.checkBoxesCam)):
			if self.checkBoxesCam[y].isChecked() == True:
				self.cam.main(self.cams[y], start, end, path, self.lineEditsCam[y].text())
				checkedRefs += self.lineEdits[y].text() + ', '


		if checkedRefs != '':
			try:
				user = getpass.getuser()
				self.slack = Slack()
				self.slack.MessageSlack(Message = 'Alembics *' + checkedRefs + '* guardado en la ruta: *' + path + '* del usuario `' + user + '`', channel = 'alembics')
			except:
				pass


	def getPath(self):
		path = AlembicUtils().path()
		self.window.txt_path.setText(path)

	def geoSelectSignal(self, num):
		state = self.checkBoxes[num].isChecked()

		if state == True:
			self.geo.selectGeoFromRef(self.refs[num])

		else:
			self.geo.clearSel()

		self.countLabel()

	def camSelectSignal(self, num):
		state = self.checkBoxesCam[num].isChecked()
		if state == True:
			self.cam.selectObj(self.cams[num])

		else:
			self.cam.clearSel()

		self.countLabel()

	def countLabel(self):

		statusStr = ''

		avCheckBoxes = self.checkBoxes + self.checkBoxesCam

		reference = False
		cameras = False

		count = 0
		for cb in self.checkBoxes:
			if cb.isChecked():
				reference = True
				count += 1


		countCam = 0
		for cbCam in self.checkBoxesCam:
			if cbCam.isChecked():
				cameras = True
				countCam += 1 

		if reference == True:
			statusStr += str(count) + ' references to export '

		if cameras == True:
			statusStr += '' + str(countCam) + ' cams to export'

		self.window.lbl_status.setText(statusStr)

	def readLocalInfo(self, file, text):
		if os.path.exists(file + '.mkf'):
			with open(file + '.mkf' ,'r') as f:
				data = f.read()
			text.setText(data)
			return True
		else:
			return False

	def writeLocalInfo(self, file, text):
		print '#####'
		print file
		with open(file + '.mkf','w') as f:

			data = f.write(text)

