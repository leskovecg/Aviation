from PyQt5 import QtCore, QtGui, QtWidgets

## https://www.youtube.com/watch?v=11iUOBqqjtU&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=20

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 396)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.red_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.red_checkBox.setGeometry(QtCore.QRect(110, 70, 91, 21))
        self.red_checkBox.setObjectName("red_checkBox")
        self.blue_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.blue_checkBox.setGeometry(QtCore.QRect(110, 100, 91, 21))
        self.blue_checkBox.setObjectName("blue_checkBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.checked())
        self.pushButton.setGeometry(QtCore.QRect(110, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 200, 131, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 384, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # set red checked by default 
        self.red_checkBox.setChecked(True)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.red_checkBox.setText(_translate("MainWindow", "red"))
        self.blue_checkBox.setText(_translate("MainWindow", "blue"))
        self.pushButton.setText(_translate("MainWindow", "submit"))
        self.label.setText(_translate("MainWindow", "pick color.."))

    def checked(self):
        if self.red_checkBox.isChecked() == True:
            self.red = "Red"
        else:
            self.red = ""
            
        if self.blue_checkBox.isChecked() == True:
            self.blue ="Blue"
        else:
            self.blue = ""
        
        self.label.setText(f'{self.red} {self.blue}')
            
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
