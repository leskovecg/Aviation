#####################################################################################
#                                                                                   #
#                              MERILNI SISTEM:                                      #
#                           AVTOR: GAŠPER LESKOVEC                                  #
#                            VERZIJA 1: 25.1.2022                                   #
#                                                                                   #
#                                                                                   #
#                                                                                   #
#####################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        ## GLAVNO OKNO:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1349, 840)
        
        ## CENTRAL WIDGET:
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        ## OKNO Z GRAFI:
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(520, 30, 731, 701))
        self.graphicsView.setObjectName("graphicsView")
        
        ## GUMB START:
        self.start_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.start_pushButton.setGeometry(QtCore.QRect(30, 80, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.start_pushButton.setFont(font)
        self.start_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.start_pushButton.setObjectName("start_pushButton")
        self.start_pushButton.pressed.connect(self.start_gumb) ## to smo dodal
        
        ## GUMB STOP:
        self.stop_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stop_pushButton.setGeometry(QtCore.QRect(30, 150, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.stop_pushButton.setFont(font)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.stop_pushButton.pressed.connect(self.stop_gumb) ## to smo dodal
        
        
        ## LCD: ČAS DO KONCA MERITVE:
        self.cas_do_konca_meritve_lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.cas_do_konca_meritve_lcdNumber.setGeometry(QtCore.QRect(30, 600, 180, 110))
        self.cas_do_konca_meritve_lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cas_do_konca_meritve_lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.cas_do_konca_meritve_lcdNumber.setLineWidth(2)
        self.cas_do_konca_meritve_lcdNumber.setSmallDecimalPoint(False)
        self.cas_do_konca_meritve_lcdNumber.setDigitCount(5)
        self.cas_do_konca_meritve_lcdNumber.setObjectName("cas_do_konca_meritve_lcdNumber")
        
        ## LABEL ZA ZAČETEK/USTAVI IZRIS:
        self.zacetek_ustavi_izrisovanje_label = QtWidgets.QLabel(self.centralwidget)
        self.zacetek_ustavi_izrisovanje_label.setGeometry(QtCore.QRect(30, 30, 301, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.zacetek_ustavi_izrisovanje_label.setFont(font)
        self.zacetek_ustavi_izrisovanje_label.setObjectName("zacetek_ustavi_izrisovanje_label")
        
        ## LCD: ŠTEVILO MERITEV:
        self.stevilo_meritev_lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.stevilo_meritev_lcdNumber.setGeometry(QtCore.QRect(290, 600, 180, 110))
        self.stevilo_meritev_lcdNumber.setLineWidth(2)
        self.stevilo_meritev_lcdNumber.setObjectName("stevilo_meritev_lcdNumber")
        
        ## LABEL ZA ČAS DO KONCA MERITVE:
        self.cas_do_konca_meritve_label = QtWidgets.QLabel(self.centralwidget)
        self.cas_do_konca_meritve_label.setGeometry(QtCore.QRect(30, 560, 231, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.cas_do_konca_meritve_label.setFont(font)
        self.cas_do_konca_meritve_label.setObjectName("cas_do_konca_meritve_label")
        
        ## LABEL ZA ŠTEVILO MERITEV:
        self.stevilo_meritev_label = QtWidgets.QLabel(self.centralwidget)
        self.stevilo_meritev_label.setGeometry(QtCore.QRect(290, 560, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.stevilo_meritev_label.setFont(font)
        self.stevilo_meritev_label.setObjectName("stevilo_meritev_label")
        
        ## LABEL ZA IME MERITVE:
        self.ime_meritve_label = QtWidgets.QLabel(self.centralwidget)
        self.ime_meritve_label.setGeometry(QtCore.QRect(30, 350, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.ime_meritve_label.setFont(font)
        self.ime_meritve_label.setObjectName("ime_meritve_label")
        
        ## GUMB ZA OK
        self.ok_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ok_pushButton.setGeometry(QtCore.QRect(30, 440, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ok_pushButton.setFont(font)
        self.ok_pushButton.setObjectName("ok_pushButton")
        self.ok_pushButton.pressed.connect(self.ok_gumb) ## to smo dodal
        
        
        ## VNOSNO POLJE ZA IME MERITVE:
        self.ime_meritve_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ime_meritve_lineEdit.setGeometry(QtCore.QRect(30, 380, 431, 41))
        self.ime_meritve_lineEdit.setObjectName("ime_meritve_lineEdit")
        
        ## LABEL ZA CAS MERJENJA:
        self.nastavi_cas_merjenja_label = QtWidgets.QLabel(self.centralwidget)
        self.nastavi_cas_merjenja_label.setGeometry(QtCore.QRect(30, 260, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.nastavi_cas_merjenja_label.setFont(font)
        self.nastavi_cas_merjenja_label.setObjectName("nastavi_cas_merjenja_label")
        
        ## LINIJA 1:
        self.line1 = QtWidgets.QFrame(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(10, 220, 481, 31))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        
        ## VNOSNO POLJE ZA NASTAVI ČAS MERJENJA:
        self.nastavi_cas_merjenja_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nastavi_cas_merjenja_lineEdit.setGeometry(QtCore.QRect(30, 300, 431, 41))
        self.nastavi_cas_merjenja_lineEdit.setObjectName("nastavi_cas_merjenja_lineEdit")
        
        ## LINIJA 2:
        self.line2 = QtWidgets.QFrame(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(10, 519, 481, 31))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        
        ## LINIJA 3:
        self.line3 = QtWidgets.QFrame(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(479, -10, 31, 821))
        self.line3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")
        
        ## RAW DATA CHECK BOX:
        self.raw_data_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.raw_data_checkBox.setGeometry(QtCore.QRect(520, 740, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.raw_data_checkBox.setFont(font)
        self.raw_data_checkBox.setObjectName("raw_data_checkBox")
        self.raw_data_checkBox.pressed.connect(self.check_box_gumb) ## to smo dodal
        
        
        #MainWindow.setCentralWidget(self.centralwidget)
        
        ## MENU BAR:
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1349, 26))
        self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        
        ## STATUS BAR:
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MERILNI SISTEM:"))
        self.start_pushButton.setText(_translate("MainWindow", "START"))
        self.stop_pushButton.setText(_translate("MainWindow", "STOP"))
        self.zacetek_ustavi_izrisovanje_label.setText(_translate("MainWindow", "Začni/ustavi izrisovanje:"))
        self.cas_do_konca_meritve_label.setText(_translate("MainWindow", "Čas merjenja:"))
        self.stevilo_meritev_label.setText(_translate("MainWindow", "Število meritev:"))
        self.ime_meritve_label.setText(_translate("MainWindow", "Ime meritve:"))
        self.ok_pushButton.setText(_translate("MainWindow", "OK"))
        self.nastavi_cas_merjenja_label.setText(_translate("MainWindow", "Nastavi čas merjenja:"))
        self.raw_data_checkBox.setText(_translate("MainWindow", "Raw data"))