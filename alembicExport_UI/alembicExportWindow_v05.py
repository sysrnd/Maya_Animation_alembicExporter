# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'C:\Users\ASUSarturo\Desktop\RnD\MKF\Animacion\Maya_Animation_alembicExporter\alembicExport_UI\Resources\alembicExportWindow_v05.ui'

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

        window_alembicExport.resize(451, 427)

        self.lyt_main = QtWidgets.QWidget(window_alembicExport)

        self.lyt_main.setObjectName("lyt_main")

        self.gridLayout = QtWidgets.QGridLayout(self.lyt_main)

        self.gridLayout.setObjectName("gridLayout")

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

        self.lyt_grid_geo = QtWidgets.QGridLayout()

        self.lyt_grid_geo.setObjectName("lyt_grid_geo")

        self.lbl_alembicGeo = QtWidgets.QLabel(self.tab_geo)

        font = QtGui.QFont()

        font.setPointSize(9)

        font.setBold(True)

        font.setWeight(75)

        self.lbl_alembicGeo.setFont(font)

        self.lbl_alembicGeo.setObjectName("lbl_alembicGeo")

        self.lyt_grid_geo.addWidget(self.lbl_alembicGeo, 0, 1, 1, 1)

        self.verticalLayout_3.addLayout(self.lyt_grid_geo)

        self.tabs_widget.addTab(self.tab_geo, "")

        self.tab_cams = QtWidgets.QWidget()

        self.tab_cams.setObjectName("tab_cams")

        self.verticalLayout = QtWidgets.QGridLayout(self.tab_cams)

        self.verticalLayout.setObjectName("verticalLayout")

        self.lyt_grid_cams = QtWidgets.QGridLayout()

        self.lyt_grid_cams.setObjectName("lyt_grid_cams")

        self.lbl_alembicCams = QtWidgets.QLabel(self.tab_cams)

        font = QtGui.QFont()

        font.setPointSize(9)

        font.setBold(True)

        font.setWeight(75)

        self.lbl_alembicCams.setFont(font)

        self.lbl_alembicCams.setObjectName("lbl_alembicCams")

        self.lyt_grid_cams.addWidget(self.lbl_alembicCams, 0, 0, 1, 1)

        self.verticalLayout.addLayout(self.lyt_grid_cams, 0, 1, 1, 1)

        self.tabs_widget.addTab(self.tab_cams, "")

        self.tab_Sel = QtWidgets.QWidget()

        self.tab_Sel.setObjectName("tab_Sel")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_Sel)

        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.lbl_selExport = QtWidgets.QLabel(self.tab_Sel)

        font = QtGui.QFont()

        font.setPointSize(9)

        font.setBold(True)

        font.setWeight(75)

        self.lbl_selExport.setFont(font)

        self.lbl_selExport.setObjectName("lbl_selExport")

        self.verticalLayout_4.addWidget(self.lbl_selExport)

        self.list_currentSel = QtWidgets.QListWidget(self.tab_Sel)

        self.list_currentSel.setObjectName("list_currentSel")

        self.verticalLayout_4.addWidget(self.list_currentSel)

        self.tabs_widget.addTab(self.tab_Sel, "")

        self.tab_config = QtWidgets.QWidget()

        self.tab_config.setObjectName("tab_config")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_config)

        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.chkBox_fileExplorer = QtWidgets.QCheckBox(self.tab_config)

        font = QtGui.QFont()

        font.setBold(True)

        font.setWeight(75)

        self.chkBox_fileExplorer.setFont(font)

        self.chkBox_fileExplorer.setObjectName("chkBox_fileExplorer")

        self.verticalLayout_2.addWidget(self.chkBox_fileExplorer)

        self.tabs_widget.addTab(self.tab_config, "")

        self.lyt_vertical_references.addWidget(self.tabs_widget)

        self.lyt_grid_references = QtWidgets.QGridLayout()

        self.lyt_grid_references.setObjectName("lyt_grid_references")

        self.lyt_vertical_references.addLayout(self.lyt_grid_references)

        self.gridLayout.addLayout(self.lyt_vertical_references, 0, 0, 1, 1)

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

        self.btn_exportAlembic.setMinimumSize(QtCore.QSize(0, 80))

        font = QtGui.QFont()

        font.setPointSize(11)

        self.btn_exportAlembic.setFont(font)

        self.btn_exportAlembic.setObjectName("btn_exportAlembic")

        self.lyt_vertical_bottom.addWidget(self.btn_exportAlembic)

        self.lbl_status = QtWidgets.QLabel(self.lyt_main)

        self.lbl_status.setObjectName("lbl_status")

        self.lyt_vertical_bottom.addWidget(self.lbl_status)

        self.progressBar = QtWidgets.QProgressBar(self.lyt_main)

        self.progressBar.setProperty("value", 24)

        self.progressBar.setObjectName("progressBar")

        self.lyt_vertical_bottom.addWidget(self.progressBar)

        self.gridLayout.addLayout(self.lyt_vertical_bottom, 1, 0, 1, 1)

        window_alembicExport.setCentralWidget(self.lyt_main)

        self.menubar = QtWidgets.QMenuBar(window_alembicExport)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 21))

        self.menubar.setObjectName("menubar")

        window_alembicExport.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(window_alembicExport)

        self.statusbar.setObjectName("statusbar")

        window_alembicExport.setStatusBar(self.statusbar)



        self.retranslateUi(window_alembicExport)

        self.tabs_widget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(window_alembicExport)



    def retranslateUi(self, window_alembicExport):

        window_alembicExport.setWindowTitle(_translate("window_alembicExport", "MKF_alembicExport", None))

        self.lbl_alembicGeo.setText(_translate("window_alembicExport", "Available references to Export", None))

        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.tab_geo), _translate("window_alembicExport", "Geometry", None))

        self.lbl_alembicCams.setText(_translate("window_alembicExport", "Available cameras to export", None))

        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.tab_cams), _translate("window_alembicExport", "Cameras", None))

        self.lbl_selExport.setText(_translate("window_alembicExport", "Current selection to Export", None))

        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.tab_Sel), _translate("window_alembicExport", "Selection", None))

        self.chkBox_fileExplorer.setText(_translate("window_alembicExport", "Open File Explorer after exporting", None))

        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.tab_config), _translate("window_alembicExport", "Config", None))

        self.lbl_endFrame.setText(_translate("window_alembicExport", "End frame", None))

        self.lbl_startFrame.setText(_translate("window_alembicExport", "Start frame", None))

        self.btn_path.setText(_translate("window_alembicExport", "Path", None))

        self.lbl_AlembicPath.setText(_translate("window_alembicExport", "Alembic Path", None))

        self.btn_exportAlembic.setText(_translate("window_alembicExport", "Export Alembics", None))

        self.lbl_status.setText(_translate("window_alembicExport", "//", None))



