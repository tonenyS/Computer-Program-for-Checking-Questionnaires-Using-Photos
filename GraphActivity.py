from PyQt5 import QtCore, QtGui, QtWidgets
from qgraphmatplotlib import QGraphMatplotlib
import os

class Ui_GraphActivity(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.root = os.path.dirname(os.path.realpath(__file__))

    def initUI(self):
        self.setObjectName("GraphActivity")
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.resize(900, 500)
        self.setMinimumSize(QtCore.QSize(480, 280))
        self.setMaximumSize(QtCore.QSize(900, 500))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("")
        self.setAutoFillBackground(False)
        self.setStyleSheet("QWidget{\n"
"    background-color:rgb(241,241,241);\n"
"}")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 881, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphPanal = QGraphMatplotlib(self.gridLayoutWidget)
        self.graphPanal.setObjectName("graphPanal")
        self.gridLayout.addWidget(self.graphPanal, 0, 0, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(self)
