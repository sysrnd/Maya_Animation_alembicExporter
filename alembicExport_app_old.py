"""
StandAlone pyqt4

"""
import sys
import platform
from PyQt4 import QtCore, QtGui
import Animacion.Maya_animation_AlembicExporter.alembicExport_UI.alembicExportWindow_v03
reload(Animacion.Maya_animation_AlembicExporter.alembicExport_UI.alembicExportWindow_v03)
from Animacion.Maya_animation_AlembicExporter.alembicExport_UI.alembicExportWindow_v03 import Ui_window_alembicExport
import Animacion.Maya_animation_AlembicExporter.alembicExport_Core.alembicExportBridge
reload(Animacion.Maya_animation_AlembicExporter.alembicExport_Core.alembicExportBridge)
from Animacion.Maya_animation_AlembicExporter.alembicExport_Core.alembicExportBridge import *#import alembicExportBridge
#reload(MKF_alembicExport.alembicExport_Core.alembicExportBridge)


#Por ventana que hayas disenado

class MyApplication(QtGui.QMainWindow, Ui_window_alembicExport):

	def __init__(self, parent=None):
		super(MyApplication, self).__init__(parent)
		self.setupUi(self)

if __name__ != "__main__":
	try:
		app = QtGui.QApplication(sys.argv)
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
