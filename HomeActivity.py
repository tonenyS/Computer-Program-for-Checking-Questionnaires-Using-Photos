# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/HomeActivity.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from qgraphmatplotlib import QGraphMatplotlib
from glob import glob
from SurveyFormer import SurveyFormer,OrderOfForm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import uuid 
import numpy as np
import os

class Ui_HomeActivity(QtWidgets.QFrame):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.root = os.path.dirname(os.path.realpath(__file__))

    def initUI(self):
        self.setObjectName("HomeActivity")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(900, 500)
        self.setMinimumSize(QtCore.QSize(480, 280))
        self.setMaximumSize(QtCore.QSize(900, 500))
        self.setWindowTitle("")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setAutoFillBackground(False)
        self.setStyleSheet("QWidget{\n"
"    background-color:rgb(241,241,241);\n"
"}")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 641, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.QGraphMatplot = QtWidgets.QLabel(self.gridLayoutWidget)
        self.QGraphMatplot.setStyleSheet("border:{\n"
"border: 1px solid  #000;\n"
"}")
        self.QGraphMatplot.setObjectName("QGraphMatplot")
        self.QGraphMatplot.setText("")
        self.gridLayout.addWidget(self.QGraphMatplot, 0, 0, 1, 1)
        self.btnSelect = QtWidgets.QPushButton(self)
        self.btnSelect.setGeometry(QtCore.QRect(670, 10, 211, 51))
        self.btnSelect.setStyleSheet("QPushButton {\n"
"border-radius:20px;\n"
"background: rgb(254, 255, 255);\n"
"color: rgb(29, 58, 143);\n"
"width: 100%;\n"
"border: 1px solid  rgba(0, 0, 0, 0.1);\n"
"outline: none;\n"
"font-size:16px;\n"
"box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);\n"
"}\n"
"QPushButton:hover{\n"
"background: rgb(29, 58, 143);\n"
"color:#ffffff;\n"
"cursor: hand;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/directory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSelect.setIcon(icon)
        self.btnSelect.setIconSize(QtCore.QSize(32, 32))
        self.btnSelect.setObjectName("btnSelect")
        self.btnSelect.clicked.connect(self.openFileNameDialog)
        self.btnStart = QtWidgets.QPushButton(self)
        self.btnStart.setGeometry(QtCore.QRect(670, 70, 211, 51))
        self.btnStart.setStyleSheet("QPushButton {\n"
"border-radius:20px;\n"
"background: rgb(254, 255, 255);\n"
"color: rgb(29, 58, 143);\n"
"width: 100%;\n"
"border: 1px solid  rgba(0, 0, 0, 0.1);\n"
"outline: none;\n"
"font-size:16px;\n"
"box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);\n"
"}\n"
"QPushButton:hover{\n"
"background: rgb(29, 58, 143);\n"
"color:#ffffff;\n"
"cursor: hand;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStart.setIcon(icon1)
        self.btnStart.setEnabled(False)
        self.btnStart.setIconSize(QtCore.QSize(32, 32))
        self.btnStart.setObjectName("btnStart")
        self.btnStart.clicked.connect(self.recognizerSurveyForm)
        self.btnSelect.setText("Select Directory")
        self.btnStart.setText("Start Process")
        self.show()

    def openFileNameDialog(self):
        self.fileName = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select directory')
        if self.fileName:
            print(self.fileName)
            self.btnStart.setEnabled(True)

    def recognizerSurveyForm(self):
        if self.fileName:
            self.file = glob(self.fileName+'/*') 
        else:
            print("ERROR -1 Dosen't have any file.")
        for f in self.file:
            fileName = uuid.uuid1()
            detector = SurveyFormer(path=f,order=OrderOfForm.Descending).recognizer()
            detector = cv2.cvtColor(detector, cv2.COLOR_GRAY2RGB)
            cv2.imwrite(f"img/paper/{fileName}.png",detector)
            pixmap = QtGui.QPixmap(f"img/paper/{fileName}.png")
            self.QGraphMatplot.setPixmap(pixmap)
            self.QGraphMatplot.setFixedSize(512, 512)
            self.show()
        self.btnStart.setEnabled(False)

