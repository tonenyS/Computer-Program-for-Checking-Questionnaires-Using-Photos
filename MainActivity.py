import ControlActivity, HomeActivity
import os
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    SurveyForm = QtWidgets.QMainWindow()
    ui = ControlActivity.Ui_SurveyForm()
    ui.setupUi(SurveyForm)
    SurveyForm.show()
    sys.exit(app.exec_())
