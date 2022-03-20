from PyQt5 import QtCore, QtGui, QtWidgets

## https://www.youtube.com/watch?v=emwXHvtAYzs&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=18

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(90, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 80, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(90, 120, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.select())
        self.pushButton.setGeometry(QtCore.QRect(70, 180, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 250, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # set default radio button to checked
        self.radioButton.setChecked(True)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "peperoni"))
        self.radioButton_2.setText(_translate("MainWindow", "cheese"))
        self.radioButton_3.setText(_translate("MainWindow", "mushroom"))
        self.pushButton.setText(_translate("MainWindow", "pick topping"))
        self.label.setText(_translate("MainWindow", "choose your top"))

    def select(self):
        #self.label.setText("Helou !")
        if self.radioButton.isChecked():
            self.label.setText("Pepperoni")
            
        if self.radioButton_2.isChecked():
            self.label.setText("Cheese")
            self.radioButton_2.setText("SELECTED")
            
        if self.radioButton_3.isChecked():
            self.label.setText(self.radioButton_3.text())
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
