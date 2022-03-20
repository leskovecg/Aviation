""" import serial

device      = 'COM4'
baud        = 9600

stevec = 0

with serial.Serial(device,baud, timeout = 0) as serialPort:
    while True:
        line = serialPort.readline()
        line = line.decode("utf-8")
        if line:
            print(line)
            
        stevec += 1 """
        
import serial

device = 'COM4'
baud = 9600

with serial.Serial(device, baud) as port:
    while True:
        print(port.readline().decode("utf-8"))