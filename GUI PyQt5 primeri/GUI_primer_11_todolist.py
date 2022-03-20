from PyQt5 import QtCore, QtGui, QtWidgets

## https://www.youtube.com/watch?v=EFKI9bu4lrY&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=13

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.additem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add_it())
        self.additem_pushButton.setGeometry(QtCore.QRect(12, 97, 241, 61))
        self.additem_pushButton.setObjectName("additem_pushButton")
        self.deleteitem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.delete_it())
        self.deleteitem_pushButton.setGeometry(QtCore.QRect(270, 100, 261, 61))
        self.deleteitem_pushButton.setObjectName("deleteitem_pushButton")
        self.clearall_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clear_it())
        self.clearall_pushButton.setGeometry(QtCore.QRect(550, 100, 231, 61))
        self.clearall_pushButton.setObjectName("clearall_pushButton")
        self.additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(12, 11, 771, 71))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 170, 771, 381))
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # add item to list
    def add_it(self):
        # grab item from the box
        item = self.additem_lineEdit.text()
        
        # add item to list
        self.mylist_listWidget.addItem(item) 
        
        # clear the item box
        self.additem_lineEdit.setText("")
        
    # delete it from list
    def delete_it(self):
        # grab the selected row or current row
        clicked = self.mylist_listWidget.currentRow()
        
        # delete selected row
        self.mylist_listWidget.takeItem(clicked)        
    
    # clear all items from list
    def clear_it(self):
        self.mylist_listWidget.clear()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.additem_pushButton.setText(_translate("MainWindow", "add item to list"))
        self.deleteitem_pushButton.setText(_translate("MainWindow", "delete item from list"))
        self.clearall_pushButton.setText(_translate("MainWindow", "clear list"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
