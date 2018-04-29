# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\RnD\Pipeline\Maya\Scripts\MKF_alembicExport\alembicExport_UI\Resources\alembicExportWindow_v02.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_window_alembicExport(object):
    def setupUi(self, window_alembicExport):
        window_alembicExport.setObjectName(_fromUtf8("window_alembicExport"))
        window_alembicExport.resize(800, 600)
        self.lyt_main = QtGui.QWidget(window_alembicExport)
        self.lyt_main.setObjectName(_fromUtf8("lyt_main"))
        self.verticalLayout = QtGui.QVBoxLayout(self.lyt_main)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lyt_vertical_references = QtGui.QVBoxLayout()
        self.lyt_vertical_references.setContentsMargins(-1, 0, -1, -1)
        self.lyt_vertical_references.setObjectName(_fromUtf8("lyt_vertical_references"))
        self.lyt_grid_references = QtGui.QGridLayout()
        self.lyt_grid_references.setObjectName(_fromUtf8("lyt_grid_references"))
        self.lyt_vertical_references.addLayout(self.lyt_grid_references)
        self.verticalLayout.addLayout(self.lyt_vertical_references)
        self.lyt_vertical_bottom = QtGui.QVBoxLayout()
        self.lyt_vertical_bottom.setObjectName(_fromUtf8("lyt_vertical_bottom"))
        self.lyt_middle = QtGui.QGridLayout()
        self.lyt_middle.setObjectName(_fromUtf8("lyt_middle"))
        self.lbl_endFrame = QtGui.QLabel(self.lyt_main)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_endFrame.setFont(font)
        self.lbl_endFrame.setObjectName(_fromUtf8("lbl_endFrame"))
        self.lyt_middle.addWidget(self.lbl_endFrame, 1, 2, 1, 1)
        self.txt_endFrame = QtGui.QLineEdit(self.lyt_main)
        self.txt_endFrame.setObjectName(_fromUtf8("txt_endFrame"))
        self.lyt_middle.addWidget(self.txt_endFrame, 1, 3, 1, 1)
        self.lbl_startFrame = QtGui.QLabel(self.lyt_main)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_startFrame.setFont(font)
        self.lbl_startFrame.setObjectName(_fromUtf8("lbl_startFrame"))
        self.lyt_middle.addWidget(self.lbl_startFrame, 1, 0, 1, 1)
        self.txt_startFrame = QtGui.QLineEdit(self.lyt_main)
        self.txt_startFrame.setObjectName(_fromUtf8("txt_startFrame"))
        self.lyt_middle.addWidget(self.txt_startFrame, 1, 1, 1, 1)
        self.lyt_vertical_bottom.addLayout(self.lyt_middle)
        self.lyt_grid_path = QtGui.QGridLayout()
        self.lyt_grid_path.setObjectName(_fromUtf8("lyt_grid_path"))
        self.txt_path = QtGui.QLineEdit(self.lyt_main)
        self.txt_path.setObjectName(_fromUtf8("txt_path"))
        self.lyt_grid_path.addWidget(self.txt_path, 1, 0, 1, 1)
        self.btn_path = QtGui.QPushButton(self.lyt_main)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_path.setFont(font)
        self.btn_path.setObjectName(_fromUtf8("btn_path"))
        self.lyt_grid_path.addWidget(self.btn_path, 1, 1, 1, 1)
        self.lbl_AlembicPath = QtGui.QLabel(self.lyt_main)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_AlembicPath.setFont(font)
        self.lbl_AlembicPath.setObjectName(_fromUtf8("lbl_AlembicPath"))
        self.lyt_grid_path.addWidget(self.lbl_AlembicPath, 0, 0, 1, 1)
        self.lyt_vertical_bottom.addLayout(self.lyt_grid_path)
        self.btn_exportAlembic = QtGui.QPushButton(self.lyt_main)
        self.btn_exportAlembic.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_exportAlembic.setFont(font)
        self.btn_exportAlembic.setObjectName(_fromUtf8("btn_exportAlembic"))
        self.lyt_vertical_bottom.addWidget(self.btn_exportAlembic)
        self.lbl_status = QtGui.QLabel(self.lyt_main)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_status.setFont(font)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.lyt_vertical_bottom.addWidget(self.lbl_status)
        self.verticalLayout.addLayout(self.lyt_vertical_bottom)
        window_alembicExport.setCentralWidget(self.lyt_main)
        self.menubar = QtGui.QMenuBar(window_alembicExport)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        window_alembicExport.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(window_alembicExport)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        window_alembicExport.setStatusBar(self.statusbar)

        self.retranslateUi(window_alembicExport)
        QtCore.QMetaObject.connectSlotsByName(window_alembicExport)

    def retranslateUi(self, window_alembicExport):
        window_alembicExport.setWindowTitle(_translate("window_alembicExport", "MKF_alembicExport", None))
        self.lbl_endFrame.setText(_translate("window_alembicExport", "End frame", None))
        self.lbl_startFrame.setText(_translate("window_alembicExport", "Start frame", None))
        self.btn_path.setText(_translate("window_alembicExport", "Path", None))
        self.lbl_AlembicPath.setText(_translate("window_alembicExport", "Alembic Path", None))
        self.btn_exportAlembic.setText(_translate("window_alembicExport", "Export Alembic", None))
        self.lbl_status.setText(_translate("window_alembicExport", "//", None))

