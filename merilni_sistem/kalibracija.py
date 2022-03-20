#####################################################################################
#                                                                                   #
#                              MERILNI SISTEM:                                      #
#                           AVTOR: GAŠPER LESKOVEC                                  #
#                            VERZIJA 1: 25.1.2022                                   #
#                                                                                   #
#                                                                                   #
#                                                                                   #
#####################################################################################

import numpy as np

# teža:
sila0, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_0g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila1689, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_1689g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila2690, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_2690g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila3654, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_3654g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila4594, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_4594g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila5588, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_5588g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila6607, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_6607g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila7589, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_7589g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila8566, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_8566g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila9537, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_9537g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila10212, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_10212g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila10885, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_10885g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila11607, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_11607g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila12333, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_12333g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila13053, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_13053g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila13895, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_13895g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila14657, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_14657g.txt', usecols =(0, 1, 2, 3), unpack = True)
sila15425, _, _, _ = np.loadtxt('kalibr_in_props\kalibracija\kalibracija_15425g.txt', usecols =(0, 1, 2, 3), unpack = True)


senzor = [sila15425.mean(), sila14657.mean(), sila13895.mean(), sila13053.mean(), sila12333.mean(), sila11607.mean(), sila10885.mean(), 
          sila10212.mean(), sila9537.mean(), sila8566.mean(), sila7589.mean(), sila6607.mean(), sila5588.mean(), sila4594.mean(), 
          sila3654.mean(), sila2690.mean(), sila1689.mean(), sila0.mean()]

sila = [151.27, 143.74, 136.26, 128.01, 120.95, 113.83, 106.75, 100.15, 93.53, 84.00, 74.42, 64.79, 54.79, 45.05, 35.83, 26.38, 16.56, 0]

## merilni lističi:
def kalibracija_sile(meritev):
    Sila = np.interp(meritev, senzor, sila)
    return Sila

## pitotka:
def kalibracija_hitrosti(meritev):
    Hitrost =  2*meritev ## spremeni
    return Hitrost

