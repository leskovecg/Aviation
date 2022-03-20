from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

## https://www.youtube.com/watch?v=4wplGk935r8&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=15

## create a database or connect to one:
conn = sqlite3.connect('mylist.db')
# create a cursor:
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE if not exists todo_list(list_item text)""")

# commit the changes
conn.commit()

# close our connection
conn.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 600)
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
        self.additem_lineEdit.setGeometry(QtCore.QRect(12, 11, 1031, 71))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 170, 1031, 381))
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        self.savedb_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.save_it())
        self.savedb_pushButton.setGeometry(QtCore.QRect(790, 100, 251, 61))
        self.savedb_pushButton.setObjectName("savedb_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # grab all the items from the database
        self.grab_all()
    
    # grab items from database
    def grab_all(self):
        ## create a database or connect to one:
        conn = sqlite3.connect('mylist.db')
        # create a cursor:
        c = conn.cursor()

        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()

        # commit the changes
        conn.commit()

        # close our connection
        conn.close()
        
        # loop through records and add to screen 
        for record in records:
            self.mylist_listWidget.addItem(str(record[0]))
        
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
        
    # save to the database
    def save_it(self):
       
        ## create a database or connect to one:
        conn = sqlite3.connect('mylist.db')
        # create a cursor:
        c = conn.cursor()
        
        # delete everything in the database table
        c.execute('DELETE FROM todo_list;',)
        
        # create blank list to hold todo items 
        items = []
        # loop through the lsitwidget and pull out each item
        for index in range(self.mylist_listWidget.count()):
            items.append(self.mylist_listWidget.item(index))
        
        for item in items:   
            #print(item.text())
            # add stuff to the table
            c.execute("INSERT INTO todo_list VALUES(:item)", {'item': item.text(),})
            
        # commit the changes
        conn.commit()

        # close our connection
        conn.close()
        
        # pop up box
        msg = QMessageBox()
        msg.setWindowTitle("Saved to Database !!!")
        msg.setText("your todo list has been saved !!!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.additem_pushButton.setText(_translate("MainWindow", "add item to list"))
        self.deleteitem_pushButton.setText(_translate("MainWindow", "delete item from list"))
        self.clearall_pushButton.setText(_translate("MainWindow", "clear list"))
        self.savedb_pushButton.setText(_translate("MainWindow", "save to database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
