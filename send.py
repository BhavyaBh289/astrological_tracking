import serial
import time

# Replace 'COM3'
ser = serial.Serial('COM3', 9600, timeout=1)
factorx = 24
factory = 24
def send_countss(chdegx,chdegy):
    countsx = chdegx*factorx
    countsy = chdegy*factory
    ser.write(f"{countsx},{countsy}\n".encode())
    while ser.in_waiting > 0:
         print(ser.readline().decode().strip())
countsx = 15
countsy = 8

try:
    send_counts(chdegx, chdegy)
    time.sleep(5)

except KeyboardInterrupt:
    pass

finally:
    ser.close()
