
#####################################################################################
#                                                                                   #
#                              MERILNI SISTEM:                                      #
#                           AVTOR: GAŠPER LESKOVEC                                  #
#                            VERZIJA 2: 25.2.2022                                   #
#                                                                                   #
#                                                                                   #
#                                                                                   #
#####################################################################################

## reference:
## https://stackoverflow.com/questions/47044290/trying-get-a-live-plot-for-a-gui-with-pyqt5
## https://stackoverflow.com/questions/46859945/linking-live-data-from-an-arduino-to-a-lcdnumber-from-pyqt5-with-python3-5

import numpy as np
from datetime import date
import serial, time, sys, os
import serial.tools.list_ports
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg 
from ui_designer.ui_merilni_sistem_v1 import Ui_MainWindow
from kalibracija import kalibracija_sile 
from kalibracija import kalibracija_hitrosti

class GetData(QThread):
    
    dataChanged = pyqtSignal(float, float, float, float, float)
    
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.Arduino = serial.Serial("COM4", 9600)

    def __del__(self):  # part of the standard format of a QThread
        self.wait()

    def run(self):  # also a required QThread function, the working part
        self.Arduino.close() ## close port 
        self.Arduino.open() ## open port

        #self.Arduino.flush() ## po flush() so vsi podatki poslani in buffer(medpomnilnik) se sprazni
        #self.Arduino.reset_input_buffer() ## flush input buffer, discarding all its contents
        start_time = time.time()
        pavza_med_meritvami = 0.01
        stevec = 0
        
        while True:
            while self.Arduino.inWaiting() == 0: ## number of bytes in the input buffer
                pass
            try:
                Run_Time = round(time.time() - start_time, 3)
                line = self.Arduino.readline()
                string = line.decode()
                splitted_string = string.split()
                print(splitted_string)  
                
                trenutne_vrednosti = [float(i) for i in splitted_string]  
                Sila = trenutne_vrednosti[0]
                Hitrost = trenutne_vrednosti[1]
                Napetost = trenutne_vrednosti[2]
                Tok = trenutne_vrednosti[3]
                    
                stevec += 1
                
                ## pavza med meritvami (pri prvi meritvi nastavimo cas na 0):
                if stevec > 0:
                    time.sleep(pavza_med_meritvami)
                    
                self.dataChanged.emit(Sila, Hitrost, Napetost, Tok, Run_Time)

            except (KeyboardInterrupt, SystemExit, IndexError, ValueError):
                pass
            
    def stop(self):
        self.terminate()
        print("QThread terminated")


class GUI(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.setupUi(self)
        self.thread = None
        
        self.sila = []
        self.hitrost = []
        self.napetost = [] 
        self.tok = []
    
        ## naše meritve:
        self.temp_time = []
        self.temp_sila = []
        self.temp_hitrost = []
        self.temp_napetost = []
        self.temp_tok = []
        
        self.enable_run = False
        self.time_run_start = 0
        self.stevilo_meritev = 0
        self.kljukica = 0 ## za checkbox
        self.ime_datoteke = ""
        
        ## postavitev:
        layout = QHBoxLayout()
        self.win = pg.GraphicsWindow()
        layout.addWidget(self.win)
        self.graphicsView.setLayout(layout)
        
        ## sila:
        self.p_sila = self.win.addPlot(title="Sila:")
        self.p_sila = self.p_sila.plot()
        self.p_sila.setPen(pg.mkPen(color="#f8f8f8", width=1))
        
        ## hitrost:
        self.p_hitrost = self.win.addPlot(title="Hitrost:")
        self.p_hitrost = self.p_hitrost.plot()
        self.p_hitrost.setPen(pg.mkPen(color="#f8f8f8", width=1))
        
        ## naslednja vrstica:
        self.win.nextRow()
        
        ## napetost: 
        self.p_napetost = self.win.addPlot(title="Napetost:")
        self.p_napetost = self.p_napetost.plot()
        self.p_napetost.setPen(pg.mkPen(color="#ff0000", width=1))
        
        ## tok:
        self.p_tok = self.win.addPlot(title="Tok:")
        self.p_tok = self.p_tok.plot()
        self.p_tok.setPen(pg.mkPen(color="#0000ff", width=1))
        

    def onDataChanged(self, Sila, Hitrost, Napetost, Tok, Run_Time):
        
        ## omogoči printanje raw data:
        if self.kljukica == 0:
           Sila = kalibracija_sile(Sila)
           Hitrost = kalibracija_hitrosti(Hitrost)
        else:
            pass 
        
        ## LCD za število meritev:
        self.stevilo_meritev_lcdNumber.display(self.stevilo_meritev)
        
        ## rezanje plotov do neke meje (prikazuje samo nek range grafa):
        if len(self.sila) < 30:
            self.sila.append(Sila)
        else:
            self.sila = self.sila[1:] + [Sila]

        if len(self.hitrost) < 30:
            self.hitrost.append(Hitrost)
        else:
            self.hitrost = self.hitrost[1:] + [Hitrost]
            
        if len(self.napetost) < 30:
            self.napetost.append(Napetost)
        else:
            self.napetost = self.napetost[1:] + [Napetost]
            
        if len(self.tok) < 30:
            self.tok.append(Tok)
        else:
            self.tok = self.tok[1:] + [Tok]
        
        ## zapis datoteke:
        if self.enable_run == True:
            ## displaya nam čas merjenja-zaokrožen na celo število:
            self.cas_do_konca_meritve_lcdNumber.display(int(time.time() - self.time_run_start))
            self.temp_time.append(time.time() - self.time_run_start)
            self.temp_sila.append(Sila)
            self.temp_hitrost.append(Hitrost)
            self.temp_napetost.append(Napetost)
            self.temp_tok.append(Tok)
            self.stevilo_meritev += 1

            if time.time() > self.time_run_start + self.time_run:
                self.enable_run = False
                with open(f'{self.path}', 'w') as file:
                    file.write('time[s];sila[N];hitrost[kmh];napetost[V];tok[A]\n')
                    for x1, x2, x3, x4, x5 in zip(self.temp_time, self.temp_sila, self.temp_hitrost, self.temp_napetost, self.temp_tok):
                        file.write(f'{x1};{x2};{x3};{x4};{x5}\n')
        
        ## prikaz točk:  
        self.p_sila.setData(self.sila)
        self.p_hitrost.setData(self.hitrost)
        self.p_napetost.setData(self.napetost)
        self.p_tok.setData(self.tok)
        

    def start_gumb(self):
        self.thread = GetData()
        self.thread.dataChanged.connect(self.onDataChanged)
        self.thread.start()
        
    def stop_gumb(self):
        self.thread.stop()
      
    ## to so umerjeni ali raw podatki:  
    def ok_gumb(self):
        try:
            self.time_run = int(self.nastavi_cas_merjenja_lineEdit.text()) # vnosno polje za čas merjenja:
            self.enable_run = True
            self.temp_time = []
            self.time_run_start = time.time()
            self.stevilo_meritev = 0 # vsakič ko pritisneš ok se števec meritev poenostavi
            self.ime_datoteke = self.ime_meritve_lineEdit.text() # vnosno polje za ime meritve:
            self.cwd = self.create_dir()
            self.path = self.uniquify()
        except:
            print('Not integer')
      
    ## funkcija preverja, če file obstaja. Če že obstaja mu doda končnico:
    def uniquify(self):
        today = date.today().strftime("%d_%m_%Y")
        path = "C:\\Users\lesko\\OneDrive\\Namizje\\laptop\DBF\\GASPER_LESKOVEC\\merilni_sistem\\merilni_sistem_meritve\\"+today+"\\"+str(self.ime_datoteke)+".txt"
        filename, extension = os.path.splitext(path)
        counter = 1

        while os.path.exists(path):
            path = filename + " (" + str(counter) + ")" + extension
            counter += 1

        return path
    
    ## aktivacija in deaktivacija raw podatkov s kljukico:
    def check_box_gumb(self):
        if self.kljukica == 0:
            self.kljukica = 1
        else:
            self.kljukica = 0
    
    ## kopirano iz verzija_1_GUI.py:
    def create_dir(self):
        
        ## datum mapa:
        today = date.today().strftime("%d_%m_%Y")
        ## glavna mapa:
        mapa = "\\merilni_sistem\\merilni_sistem_meritve\\" + today
        
        current_dir = os.getcwd()
        complete_path = current_dir + mapa

        # Setup Output Folder
        if not os.path.isdir(complete_path):
            print("Path doesn't exist, creating one")
            try:
                os.makedirs(complete_path)
            except OSError as exc: 			# Guard against race condition
                print("Didn't create a new folder, error occurred")
        else:
            print("Folder already exists")

        return complete_path
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dyno = GUI()
    Dyno.show()
    sys.exit(app.exec_())
    
    
    
