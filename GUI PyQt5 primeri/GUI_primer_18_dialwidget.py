from PyQt5 import QtCore, QtGui, QtWidgets

## https://www.youtube.com/watch?v=sHZf729Hwgk&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=22

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(373, 398)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dial = QtWidgets.QDial(self.centralwidget)
        
        # set dial defaults
        # self.dial.setMinimum(10)
        # self.dial.setMaximum(360)
        # self.dial.setRange(100,200)
        
        # set default startup position
        # self.dial.setValue(50)
        
        # set notches
        self.dial.setNotchesVisible(True)
        
        # use Dial
        self.dial.valueChanged.connect(lambda: self.dialer())
        
        
        self.dial.setGeometry(QtCore.QRect(110, 60, 161, 161))
        self.dial.setObjectName("dial")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 250, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 373, 26))
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
        self.label.setText(_translate("MainWindow", "Current position: 0 "))

    def dialer(self):
        # grab the current dial position
        value = self.dial.value()
        
        # set label text
        self.label.setText(f'Current position: {str(value)}')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
