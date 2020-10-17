# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ControlActivity.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from HomeActivity import Ui_HomeActivity
from WelcomeActivity import Ui_WelcomeActivity
from GraphActivity import Ui_GraphActivity
import os

class Ui_SurveyForm(object):
    def setupUi(self, SurveyForm):
        SurveyForm.setObjectName("SurveyForm")
        SurveyForm.setWindowModality(QtCore.Qt.ApplicationModal)
        SurveyForm.resize(960, 540)
        SurveyForm.setMinimumSize(QtCore.QSize(960, 540))
        SurveyForm.setMaximumSize(QtCore.QSize(960, 540))
        icon = QtGui.QIcon()
        self.root = os.path.dirname(os.path.realpath(__file__))
        icon.addPixmap(QtGui.QPixmap(self.root + os.path.sep + "/img/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(self.root + os.path.sep + "/img/clipboard.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        SurveyForm.setWindowIcon(icon)
        SurveyForm.setAutoFillBackground(True)
        self.root = os.path.dirname(os.path.realpath(__file__))
        SurveyForm.setWindowIcon(QtGui.QIcon(self.root  + os.path.sep + 'img/logo.png'))
        self.centralwidget = QtWidgets.QWidget(SurveyForm)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -10, 61, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color:rgb(49, 49, 49);\n"
"display:flex;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnBar = QtWidgets.QPushButton(self.frame)
        self.btnBar.setGeometry(QtCore.QRect(0, 10, 61, 51))
        self.btnBar.setStyleSheet("/*border:1px solid #ffffff;*/\n"
"border:none;\n"
"background-color:rgb(209, 52, 56);")
        self.btnBar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.root + os.path.sep + "/img/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBar.setIcon(icon1)
        self.btnBar.setIconSize(QtCore.QSize(28, 28))
        self.btnBar.setAutoDefault(False)
        self.btnBar.setDefault(True)
        self.btnBar.setObjectName("btnBar")
        self.btnHome = QtWidgets.QPushButton(self.frame)
        self.btnHome.setGeometry(QtCore.QRect(0, 60, 61, 51))
        self.btnHome.setStyleSheet("/*border:1px solid #ffffff;*/\n"
"QPushButton:hover\n"
"{\n"
"   border:none;\n"
"   background-color:rgb(209, 52, 56);\n"
"}\n"
"QPushButton\n"
"{\n"
"   border:none;\n"
"}")
        self.btnHome.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.root + os.path.sep + "/img/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHome.setIcon(icon2)
        self.btnHome.setIconSize(QtCore.QSize(28, 28))
        self.btnHome.setAutoDefault(False)
        self.btnHome.setDefault(True)
        self.btnHome.setObjectName("btnHome")
        self.btnGraph = QtWidgets.QPushButton(self.frame)
        self.btnGraph.setGeometry(QtCore.QRect(0, 110, 61, 51))
        self.btnGraph.setStyleSheet("/*border:1px solid #ffffff;*/\n"
"QPushButton:hover\n"
"{\n"
"   border:none;\n"
"   background-color:rgb(209, 52, 56);\n"
"}\n"
"QPushButton\n"
"{\n"
"   border:none;\n"
"}")
        self.btnGraph.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(self.root + os.path.sep + "/img/earnings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGraph.setIcon(icon3)
        self.btnGraph.setIconSize(QtCore.QSize(28, 28))
        self.btnGraph.setAutoDefault(False)
        self.btnGraph.setDefault(True)
        self.btnGraph.setObjectName("btnGraph")
        self.btnGraph.clicked.connect(self.graph)
        self.btnExit = QtWidgets.QPushButton(self.frame)
        self.btnExit.setGeometry(QtCore.QRect(0, 160, 61, 51))
        self.btnExit.setStyleSheet("/*border:1px solid #ffffff;*/\n"
"QPushButton:hover\n"
"{\n"
"   border:none;\n"
"   background-color:rgb(209, 52, 56);\n"
"}\n"
"QPushButton\n"
"{\n"
"   border:none;\n"
"}")
        self.btnExit.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.root + os.path.sep + "/img/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon4)
        self.btnExit.setIconSize(QtCore.QSize(28, 28))
        self.btnExit.setAutoDefault(False)
        self.btnExit.setDefault(True)
        self.btnExit.setObjectName("btnExit")
        self.btnSetting = QtWidgets.QPushButton(self.frame)
        self.btnSetting.setGeometry(QtCore.QRect(0, 500, 61, 51))
        self.btnSetting.setStyleSheet("/*border:1px solid #ffffff;*/\n"
"QPushButton:hover\n"
"{\n"
"   border:none;\n"
"   background-color:rgb(209, 52, 56);\n"
"}\n"
"QPushButton\n"
"{\n"
"   border:none;\n"
"}")
        self.btnSetting.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(self.root + os.path.sep + "/img/customer-support.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetting.setIcon(icon5)
        self.btnSetting.setIconSize(QtCore.QSize(28, 28))
        self.btnSetting.setAutoDefault(False)
        self.btnSetting.setDefault(True)
        self.btnSetting.setObjectName("btnSetting")
        self.verticalLayout.addWidget(self.frame)
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(60, 0, 901, 541))
        self.mdiArea.setStyleSheet("background-color:#ffffff;")
        brush = QtGui.QBrush(QtGui.QColor(241, 241, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setObjectName("mdiArea")
        self.btnHome.clicked.connect(self.home)
        self.btnExit.clicked.connect(self.exit)
        self.btnBar.clicked.connect(self.welcome)
        SurveyForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(SurveyForm)
        QtCore.QMetaObject.connectSlotsByName(SurveyForm)
        self.welcome()
        

    def retranslateUi(self, SurveyForm):
        _translate = QtCore.QCoreApplication.translate
        SurveyForm.setWindowTitle(_translate("SurveyForm", "โปรแกรมช่วยคำนวณค่าสถิติจากแบบสอบถามประเภทตาราง [รุ่นทดลอง]"))
        self.btnHome.setToolTip(_translate("SurveyForm", "Home"))
        self.btnGraph.setToolTip(_translate("SurveyForm", "Graph"))
        self.btnExit.setToolTip(_translate("SurveyForm", "Exit"))
        self.btnSetting.setToolTip(_translate("SurveyForm", "Setting"))

    def exit(self):
        QtCore.QCoreApplication.exit(0)

    def home(self):
        self.clearbackgroundcolor()
        self.setbackgroundcolor(self.btnHome)
        home_ui = Ui_HomeActivity()
        self.mdiArea.addSubWindow(home_ui)
        home_ui.show()
        home_ui.setWindowState(QtCore.Qt.WindowMaximized)

    def graph(self):
        self.clearbackgroundcolor()
        self.setbackgroundcolor(self.btnGraph)
        graph_ui = Ui_GraphActivity()
        self.mdiArea.addSubWindow(graph_ui)
        graph_ui.show()
        graph_ui.setWindowState(QtCore.Qt.WindowMaximized)

    def welcome(self):
        self.clearbackgroundcolor()
        self.setbackgroundcolor(self.btnBar)
        welcome_ui = Ui_WelcomeActivity()
        self.mdiArea.addSubWindow(welcome_ui)
        welcome_ui.show()
        welcome_ui.setWindowState(QtCore.Qt.WindowMaximized)

    def clearbackgroundcolor(self):
        self.btnBar.setStyleSheet("QPushButton:hover {"
"   border:none;\n"
"   background-color:rgb(209, 52, 56);\n"
"}\n"
"QPushButton\n"
"{\n"
"   border:none;\n"
"   background-color: rgb(49, 49, 49);\n"
"}")
        self.btnGraph.setStyleSheet("QPushButton:hover {"
"   border:none;\n"
"   background-color:rgb(209, 52, 56);\n"
"}\n"
"QPushButton\n"
"{\n"
"   border:none;\n"
"   background-color: rgb(49, 49, 49);\n"
"}")
        self.btnHome.setStyleSheet("QPushButton:hover {"
"   border:none;\n"
"   background-color:rgb(209, 52, 56);\n"
"}\n"
"QPushButton\n"
"{\n"
"   border:none;\n"
"   background-color: rgb(49, 49, 49);\n"
"}")
        self.btnSetting.setStyleSheet("QPushButton:hover {"
"   border:none;\n"
"   background-color:rgb(209, 52, 56);\n"
"}\n"
"QPushButton\n"
"{\n"
"   border:none;\n"
"   background-color: rgb(49, 49, 49);\n"
"}")

    def setbackgroundcolor(self,object):
        object.setStyleSheet("QPushButton:hover {"
"   border:none;\n"
"   background-color:rgb(209, 52, 56);\n"
"}\n"
"QPushButton\n"
"{\n"
"   border:none;\n"
"   background-color: rgb(209, 52, 56);\n"
"}")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SurveyForm = QtWidgets.QMainWindow()
    ui = Ui_SurveyForm()
    ui.setupUi(SurveyForm)
    SurveyForm.show()
    sys.exit(app.exec_())
