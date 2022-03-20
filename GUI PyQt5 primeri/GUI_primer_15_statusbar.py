from PyQt5 import QtCore, QtGui, QtWidgets

## https://www.youtube.com/watch?v=m_DYnnr8N00&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=17

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 227)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.push_1())
        self.button1_pushButton.setGeometry(QtCore.QRect(30, 20, 221, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button1_pushButton.setFont(font)
        self.button1_pushButton.setObjectName("button1_pushButton")
        self.button2_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.push_2())
        self.button2_pushButton_2.setGeometry(QtCore.QRect(280, 20, 211, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button2_pushButton_2.setFont(font)
        self.button2_pushButton_2.setObjectName("button2_pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.statusBar.showMessage("ready...")
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "status bar stuff"))
        self.button1_pushButton.setText(_translate("MainWindow", "button 1"))
        self.button2_pushButton_2.setText(_translate("MainWindow", "Clear status bar"))

    def push_1(self):
        self.statusBar.showMessage("I pressed button 1")
        
    def push_2(self):
        self.statusBar.showMessage("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
