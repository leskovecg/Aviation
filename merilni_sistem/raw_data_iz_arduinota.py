import serial
import time
import numpy as np

## open serial port:
ser = serial.Serial('COM4', 9800)
## se ustavi za 2 sekundi (program se začne izvajati po 2 sekundah):
time.sleep(2)

## podatki:
sila = [] # merilni lističi
hitrost = [] # pitotka
napetost = [] 
tok = []

for n in range(100):
    
    ## reads the incoming data from the serial line, which returns a byte object:
    line = ser.readline()

    ## converting byte object to string:
    string = line.decode()

    ## splitting string:
    splitted_string = string.split()

    ## trenutne_vrednosti = (sila, hitrost, napetost, tok)
    ## trenutne vrednosti imajo na začetku vrednost 0:
    trenutne_vrednosti = np.zeros(4, dtype = float)

    ## velikokrat se zgodi da nam podatka s silo ne vrne (lističi) ?? 0.00 bi moglo registrirat??
    ## shranjevanje elementov v list trenutnih vrednosti: 
    for i in range(len(splitted_string)):
        if len(splitted_string) == 4:
            trenutne_vrednosti[i] = float(splitted_string[i])
        else:
            trenutne_vrednosti[i+1] = float(splitted_string[i])

    sila.append(trenutne_vrednosti[0])
    hitrost.append(trenutne_vrednosti[1])
    napetost.append(trenutne_vrednosti[2])
    tok.append(trenutne_vrednosti[3])
    
    ## printanje meritev vsako sekundo:
    time.sleep(1)
    print('Sila: ' + str(trenutne_vrednosti[0]) + ', hitrost: ' + str(trenutne_vrednosti[1]) + 
          ', napetost: ' + str(trenutne_vrednosti[2]) + ', tok: ' + str(trenutne_vrednosti[3])
          )
     
