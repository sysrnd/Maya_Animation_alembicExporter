"""
StandAlone pyqt4

"""
import sys


import platform


from Modules.Qt import QtCore, QtGui, QtWidgets
import Animacion.Maya_Animation_alembicExporter.alembicExport_UI.alembicExportWindow_v04
reload(Animacion.Maya_Animation_alembicExporter.alembicExport_UI.alembicExportWindow_v04)
from Animacion.Maya_Animation_alembicExporter.alembicExport_UI.alembicExportWindow_v04 import Ui_window_alembicExport

import Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExportBridge	
reload(Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExportBridge)
from Animacion.Maya_Animation_alembicExporter.alembicExport_Core.alembicExportBridge import *#import alembicExportBridge


#reload(MKF_alembicExport.alembicExport_Core.alembicExportBridge)


#Por ventana que hayas disenado

class MyApplication(QtWidgets.QMainWindow, Ui_window_alembicExport):

	def __init__(self, parent=None):
		super(MyApplication, self).__init__(parent)
		self.setupUi(self)

if __name__ != "__main__":
	try:
		app = QtWidgets.QApplication(sys.argv)
	except:
		app = QtCore.QCoreApplication.instance()
	window = MyApplication()
	window.setWindowFlags(
		window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
	interfaceMacho = alembicExportBridge(window=window)
	window.show()

	try:
		sys.exit(app.exec_())
	except:
		"error al intentar salir"


