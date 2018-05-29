import sys
import platform

from Modules.Qt import QtCore, QtGui, QtWidgets
import Animacion.Maya_Animation_alembicExporter.alembicExport_UI.alembicExportWindow_v05
reload(Animacion.Maya_Animation_alembicExporter.alembicExport_UI.alembicExportWindow_v05)
from Animacion.Maya_Animation_alembicExporter.alembicExport_UI.alembicExportWindow_v05 import Ui_window_alembicExport

import Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExportBridge	
reload(Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExportBridge)
from Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExportBridge import *#import alembicExportBridge

try:
	from shiboken import wrapInstance
except:
	from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui
import maya.cmds as cmds

def maya_main_window():
	main_window_ptr = omui.MQtUtil.mainWindow()
	return wrapInstance( long( main_window_ptr ), QtWidgets.QWidget )

class MyApplication(QtWidgets.QMainWindow, Ui_window_alembicExport):

	def __init__(self, parent= maya_main_window() ):
		
		super(MyApplication, self).__init__(parent)
		self.titleWindow = 'window_alembicExport'
		self.setupUi(self)
		self.interfaceMacho = alembicExportBridge(window=self)

	def closeEvent( self, event ):
		print 'closed'
		cmds.scriptJob( kill=self.interfaceMacho.returnScriptJob(), force=True )

if __name__ != "__main__":
	
	
	try:
		if cmds.window(window.titleWindow, exists=True):
			cmds.deleteUI(window.titleWindow)
	except:
		pass

	window = MyApplication()

	try:
		app = QtWidgets.QApplication(sys.argv)
	except:
		app = QtCore.QCoreApplication.instance()

	window.setWindowFlags(
		window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
	#interfaceMacho = alembicExportBridge(window=window)

	window.show()

