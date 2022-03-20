from nbformat import current_nbformat
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

def run(self):  
        self.Arduino.close() 
        self.Arduino.open() 
        start_time = time.time()
        pause = 0.01
        counter = 0
        
        while True:
            while self.Arduino.inWaiting() == 0: 
                pass
            try:
                Run_Time = round(time.time() - start_time, 3)
                line = self.Arduino.readline()
                string = line.decode()
                splitted_string = string.split()
                
                values = [float(i) for i in splitted_string]  
                Force = values[0]
                Velocity = values[1]
                Voltage = values[2]
                Current = values[3]
                    
                counter += 1
                
                if counter > 0:
                    time.sleep(pause)
                    
                self.dataChanged.emit(Force, Velocity, Voltage, Current, Run_Time)

            except (KeyboardInterrupt, SystemExit, IndexError, ValueError):
                pass