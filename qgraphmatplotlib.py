from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import os

class QGraphMatplotlib(QtWidgets.QWidget):

    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure())
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(self.vertical_layout)
        self.root = os.path.dirname(os.path.realpath(__file__))
        self.df = pd.read_csv(self.root + os.path.sep + "/src/export.txt")
        self.__setImage__()

    def __setImage__(self):
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.plot(self.df)
        self.canvas.axes.set_title("Summary table")