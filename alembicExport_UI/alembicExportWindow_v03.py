# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'Z:\RnD\Pipeline\Maya\Scripts\MKF_alembicExport\alembicExport_UI\Resources\alembicExportWindow_v03.ui'

#

# Created by: PyQt4 UI code generator 4.11.4

#

# WARNING! All changes made in this file will be lost!



from Modules.Qt import QtCore, QtGui, QtWidgets


try:

    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):

        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):

        return QtCore.QCoreApplication.translate(context, text, disambig)



class Ui_window_alembicExport(object):

    def setupUi(self, window_alembicExport):

        window_alembicExport.setObjectName("window_alembicExport")

        window_alembicExport.resize(400, 250)

        self.lyt_main = QtWidgets.QWidget(window_alembicExport)

        self.lyt_main.setObjectName("lyt_main")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.lyt_main)

        self.verticalLayout.setObjectName("verticalLayout")

        self.lyt_vertical_references = QtWidgets.QVBoxLayout()

        self.lyt_vertical_references.setContentsMargins(-1, 0, -1, -1)

        self.lyt_vertical_references.setObjectName("lyt_vertical_references")

        self.lyt_grid_references = QtWidgets.QGridLayout()

        self.lyt_grid_references.setObjectName("lyt_grid_references")

        self.lbl_alembicInfo = QtWidgets.QLabel(self.lyt_main)

        font = QtGui.QFont()

        font.setPointSize(9)

        font.setBold(True)

        font.setWeight(75)

        self.lbl_alembicInfo.setFont(font)

        self.lbl_alembicInfo.setObjectName("lbl_alembicInfo")

        self.lyt_grid_references.addWidget(self.lbl_alembicInfo, 0, 1, 1, 1)

        self.lyt_vertical_references.addLayout(self.lyt_grid_references)

        self.verticalLayout.addLayout(self.lyt_vertical_references)

        self.lyt_vertical_bottom = QtWidgets.QVBoxLayout()

        self.lyt_vertical_bottom.setObjectName("lyt_vertical_bottom")

        self.lyt_middle = QtWidgets.QGridLayout()

        self.lyt_middle.setObjectName("lyt_middle")

        self.lbl_endFrame = QtWidgets.QLabel(self.lyt_main)

        font = QtGui.QFont()

        font.setPointSize(9)

        self.lbl_endFrame.setFont(font)

        self.lbl_endFrame.setObjectName("lbl_endFrame")

        self.lyt_middle.addWidget(self.lbl_endFrame, 1, 2, 1, 1)

        self.txt_endFrame = QtWidgets.QLineEdit(self.lyt_main)

        self.txt_endFrame.setObjectName("txt_endFrame")

        self.lyt_middle.addWidget(self.txt_endFrame, 1, 3, 1, 1)

        self.lbl_startFrame = QtWidgets.QLabel(self.lyt_main)

        font = QtGui.QFont()

        font.setPointSize(9)

        self.lbl_startFrame.setFont(font)

        self.lbl_startFrame.setObjectName("lbl_startFrame")

        self.lyt_middle.addWidget(self.lbl_startFrame, 1, 0, 1, 1)

        self.txt_startFrame = QtWidgets.QLineEdit(self.lyt_main)

        self.txt_startFrame.setObjectName("txt_startFrame")

        self.lyt_middle.addWidget(self.txt_startFrame, 1, 1, 1, 1)

        self.lyt_vertical_bottom.addLayout(self.lyt_middle)

        self.lyt_grid_path = QtWidgets.QGridLayout()

        self.lyt_grid_path.setObjectName("lyt_grid_path")

        self.txt_path = QtWidgets.QLineEdit(self.lyt_main)

        self.txt_path.setObjectName("txt_path")

        self.lyt_grid_path.addWidget(self.txt_path, 1, 0, 1, 1)

        self.btn_path = QtWidgets.QPushButton(self.lyt_main)

        font = QtGui.QFont()

        font.setPointSize(11)

        self.btn_path.setFont(font)

        self.btn_path.setObjectName("btn_path")

        self.lyt_grid_path.addWidget(self.btn_path, 1, 1, 1, 1)

        self.lbl_AlembicPath = QtWidgets.QLabel(self.lyt_main)

        font = QtGui.QFont()

        font.setPointSize(11)

        self.lbl_AlembicPath.setFont(font)

        self.lbl_AlembicPath.setObjectName("lbl_AlembicPath")

        self.lyt_grid_path.addWidget(self.lbl_AlembicPath, 0, 0, 1, 1)

        self.lyt_vertical_bottom.addLayout(self.lyt_grid_path)

        self.btn_exportAlembic = QtWidgets.QPushButton(self.lyt_main)

        self.btn_exportAlembic.setMinimumSize(QtCore.QSize(0, 40))

        font = QtGui.QFont()

        font.setPointSize(11)

        self.btn_exportAlembic.setFont(font)

        self.btn_exportAlembic.setObjectName("btn_exportAlembic")

        self.lyt_vertical_bottom.addWidget(self.btn_exportAlembic)

        self.lbl_status = QtWidgets.QLabel(self.lyt_main)

        self.lbl_status.setObjectName("lbl_status")

        self.lyt_vertical_bottom.addWidget(self.lbl_status)

        self.verticalLayout.addLayout(self.lyt_vertical_bottom)

        window_alembicExport.setCentralWidget(self.lyt_main)

        self.menubar = QtWidgets.QMenuBar(window_alembicExport)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))

        self.menubar.setObjectName("menubar")

        window_alembicExport.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(window_alembicExport)

        self.statusbar.setObjectName("statusbar")

        window_alembicExport.setStatusBar(self.statusbar)



        self.retranslateUi(window_alembicExport)

        QtCore.QMetaObject.connectSlotsByName(window_alembicExport)



    def retranslateUi(self, window_alembicExport):

        window_alembicExport.setWindowTitle(_translate("window_alembicExport", "MKF_alembicExport", None))

        self.lbl_alembicInfo.setText(_translate("window_alembicExport", "Available references to Export", None))

        self.lbl_endFrame.setText(_translate("window_alembicExport", "End frame", None))

        self.lbl_startFrame.setText(_translate("window_alembicExport", "Start frame", None))

        self.btn_path.setText(_translate("window_alembicExport", "Path", None))

        self.lbl_AlembicPath.setText(_translate("window_alembicExport", "Alembic Path", None))

        self.btn_exportAlembic.setText(_translate("window_alembicExport", "Export Alembics", None))

        self.lbl_status.setText(_translate("window_alembicExport", "//", None))



