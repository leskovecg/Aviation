## video o tem:
## https://www.youtube.com/watch?v=5K__zwBj_nY&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=6
## convertanje iz .ui v .py:
## https://www.youtube.com/watch?v=1wEsP70hO0o  

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.push_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it())
        self.push_button.setGeometry(QtCore.QRect(170, 440, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.push_button.setFont(font)
        self.push_button.setObjectName("push_button")
        self.hello_world_label = QtWidgets.QLabel(self.centralwidget)
        self.hello_world_label.setGeometry(QtCore.QRect(110, 110, 351, 281))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.hello_world_label.setFont(font)
        self.hello_world_label.setObjectName("hello_world_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ## dopisana funkcija:
    def press_it(self):
        self.hello_world_label.setText("Boom!")
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.push_button.setText(_translate("MainWindow", "Pritisni!"))
        self.hello_world_label.setText(_translate("MainWindow", "Hello World !"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
