# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'C:\Users\ASUSarturo\Desktop\RnD\MKF\Animacion\Maya_Animation_alembicExporter\alembicExport_UI\Resources\alembicExportWindow_v04.ui'

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

        window_alembicExport.resize(451, 323)

        self.lyt_main = QtWidgets.QWidget(window_alembicExport)

        self.lyt_main.setObjectName("lyt_main")

        self.gridLayout = QtWidgets.QGridLayout(self.lyt_main)

        self.gridLayout.setObjectName("gridLayout")

        self.lyt_vertical_bottom = QtWidgets.QVBoxLayout()

        self.lyt_vertical_bottom.setObjectName("lyt_vertical_bottom")

        self.lyt_middle = QtWidgets.QGridLayout()

        self.lyt_middle.setObjectName("lyt_middle")

        self.txt_startFrame = QtWidgets.QLineEdit(self.lyt_main)

        self.txt_startFrame.setObjectName("txt_startFrame")

        self.lyt_middle.addWidget(self.txt_startFrame, 1, 1, 1, 1)

        self.lbl_endFrame = QtWidgets.QLabel(self.lyt_main)

        font = QtGui.QFont()

        font.setPointSize(9)

        self.lbl_endFrame.setFont(font)

        self.lbl_endFrame.setObjectName("lbl_endFrame")

        self.lyt_middle.addWidget(self.lbl_endFrame, 1, 2, 1, 1)

        self.lbl_startFrame = QtWidgets.QLabel(self.lyt_main)

        font = QtGui.QFont()

        font.setPointSize(9)

        self.lbl_startFrame.setFont(font)

        self.lbl_startFrame.setObjectName("lbl_startFrame")

        self.lyt_middle.addWidget(self.lbl_startFrame, 1, 0, 1, 1)

        self.txt_endFrame = QtWidgets.QLineEdit(self.lyt_main)

        self.txt_endFrame.setObjectName("txt_endFrame")

        self.lyt_middle.addWidget(self.txt_endFrame, 1, 3, 1, 1)

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

        self.btn_exportAlembic.setMinimumSize(QtCore.QSize(0, 60))

        font = QtGui.QFont()

        font.setPointSize(11)

        self.btn_exportAlembic.setFont(font)

        self.btn_exportAlembic.setObjectName("btn_exportAlembic")

        self.lyt_vertical_bottom.addWidget(self.btn_exportAlembic)

        self.lbl_status = QtWidgets.QLabel(self.lyt_main)

        self.lbl_status.setObjectName("lbl_status")

        self.lyt_vertical_bottom.addWidget(self.lbl_status)

        self.gridLayout.addLayout(self.lyt_vertical_bottom, 1, 0, 1, 1)

        self.lyt_vertical_references = QtWidgets.QVBoxLayout()

        self.lyt_vertical_references.setContentsMargins(-1, 0, -1, -1)

        self.lyt_vertical_references.setObjectName("lyt_vertical_references")

        self.tabs_widget = QtWidgets.QTabWidget(self.lyt_main)

        self.tabs_widget.setTabPosition(QtWidgets.QTabWidget.North)

        self.tabs_widget.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.tabs_widget.setElideMode(QtCore.Qt.ElideNone)

        self.tabs_widget.setDocumentMode(False)

        self.tabs_widget.setTabsClosable(False)

        self.tabs_widget.setMovable(False)

        self.tabs_widget.setObjectName("tabs_widget")

        self.tab_geo = QtWidgets.QWidget()

        self.tab_geo.setObjectName("tab_geo")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_geo)

        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.lyt_vertical_geo = QtWidgets.QGridLayout()

        self.lyt_vertical_geo.setObjectName("lyt_vertical_geo")

        self.lbl_alembicGeo = QtWidgets.QLabel(self.tab_geo)

        font = QtGui.QFont()

        font.setPointSize(9)

        font.setBold(True)

        font.setWeight(75)

        self.lbl_alembicGeo.setFont(font)

        self.lbl_alembicGeo.setObjectName("lbl_alembicGeo")

        self.lyt_vertical_geo.addWidget(self.lbl_alembicGeo, 0, 1, 1, 1)

        self.verticalLayout_3.addLayout(self.lyt_vertical_geo)

        self.tabs_widget.addTab(self.tab_geo, "")

        self.tab_cams = QtWidgets.QWidget()

        self.tab_cams.setObjectName("tab_cams")

        self.verticalLayout = QtWidgets.QGridLayout(self.tab_cams)

        self.verticalLayout.setObjectName("verticalLayout")

        self.lbl_vertical_cams = QtWidgets.QGridLayout()

        self.lbl_vertical_cams.setObjectName("lbl_vertical_cams")

        self.lbl_alembicCams = QtWidgets.QLabel(self.tab_cams)

        font = QtGui.QFont()

        font.setPointSize(9)

        font.setBold(True)

        font.setWeight(75)

        self.lbl_alembicCams.setFont(font)

        self.lbl_alembicCams.setObjectName("lbl_alembicCams")

        self.lbl_vertical_cams.addWidget(self.lbl_alembicCams)

        self.verticalLayout.addLayout(self.lbl_vertical_cams, 0, 1, 1, 1)

        self.lbl_alembicCams.raise_()

        self.tabs_widget.addTab(self.tab_cams, "")

        self.lyt_vertical_references.addWidget(self.tabs_widget)

        self.lyt_grid_references = QtWidgets.QGridLayout()

        self.lyt_grid_references.setObjectName("lyt_grid_references")

        self.lyt_vertical_references.addLayout(self.lyt_grid_references)

        self.gridLayout.addLayout(self.lyt_vertical_references, 0, 0, 1, 1)

        window_alembicExport.setCentralWidget(self.lyt_main)

        self.menubar = QtWidgets.QMenuBar(window_alembicExport)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 21))

        self.menubar.setObjectName("menubar")

        window_alembicExport.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(window_alembicExport)

        self.statusbar.setObjectName("statusbar")

        window_alembicExport.setStatusBar(self.statusbar)



        self.retranslateUi(window_alembicExport)

        self.tabs_widget.setCurrentIndex(1)

        QtCore.QMetaObject.connectSlotsByName(window_alembicExport)



    def retranslateUi(self, window_alembicExport):

        window_alembicExport.setWindowTitle(_translate("window_alembicExport", "MKF_alembicExport", None))

        self.lbl_endFrame.setText(_translate("window_alembicExport", "End frame", None))

        self.lbl_startFrame.setText(_translate("window_alembicExport", "Start frame", None))

        self.btn_path.setText(_translate("window_alembicExport", "Path", None))

        self.lbl_AlembicPath.setText(_translate("window_alembicExport", "Alembic Path", None))

        self.btn_exportAlembic.setText(_translate("window_alembicExport", "Export Alembics", None))

        self.lbl_status.setText(_translate("window_alembicExport", "//", None))

        self.lbl_alembicGeo.setText(_translate("window_alembicExport", "Available references to Export", None))

        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.tab_geo), _translate("window_alembicExport", "Geometry", None))

        self.lbl_alembicCams.setText(_translate("window_alembicExport", "Available cameras to export", None))

        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.tab_cams), _translate("window_alembicExport", "Cameras", None))



