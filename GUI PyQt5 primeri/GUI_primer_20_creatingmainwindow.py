from PyQt5 import QtCore, QtGui, QtWidgets
from GUI_primer_20_creatingmainwindow2 import Ui_SecondWindow
from GUI_primer_20_creatingmainwindow3 import Ui_Dialog

## https://www.youtube.com/watch?v=R5N8TA0KFxc&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=24

# open dialog window
class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    """     
    # open main window
    class Ui_MainWindow(object):
        def openWindow(self):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SecondWindow()
            self.ui.setupUi(self.window)
            self.window.show()"""
       
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 315)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(170, 140, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open Window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
