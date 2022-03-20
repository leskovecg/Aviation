from PyQt5 import QtCore, QtGui, QtWidgets

## https://www.youtube.com/watch?v=31QT25J_cec&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=23

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 100, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clicker())
        self.pushButton.setGeometry(QtCore.QRect(380, 97, 111, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # make combo box clickable
        self.comboBox.activated.connect(self.clicker)
        
        # add items to combo box
        self.comboBox.addItem("Pepperoni")
        self.comboBox.addItem("Mushroom")
        self.comboBox.addItem("Cheese")
        self.comboBox.addItem("Onion")
        
        # add a list
        my_toppings = ['Ham', 'Pinneaple', 'Supreme']
        self.comboBox.addItems(my_toppings)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "select item from combo box"))
        self.pushButton.setText(_translate("MainWindow", "select"))

    def clicker(self):
        self.label.setText(f'you picked: {self.comboBox.currentText()}')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
