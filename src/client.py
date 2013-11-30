import socket
import time
from threading import Thread
import os


def adjustVelocity(velocity):
    velocityTmp = velocity
    for i in ["b/s", "KB/s","MB/s","GB/s"]:
        if velocityTmp < 1024:
            return str("%.2f" %velocityTmp) + i
        velocityTmp *= 0.001
        
def adjustSize(size):
    sizeTmp = size*1024
    for i in ["b", "KB","MB","GB"]:
        if sizeTmp < 1024:
            return str("%.2f" %sizeTmp) + i
        sizeTmp /= 1024.
        
def drawProgress(progress):
    totalBar = (60*int(progress))/100
    bar = "[" + "="*totalBar + (">" if  totalBar < (60) else "") + " "*(60-totalBar)
    bar += "] %.2f%%" %(progress) 
    print bar
    
def velocityCalculate():
    global previousBytesReceive,currentBytesReceive,previousTime,currentTime 
    while True:
        time.sleep(0.5)
        os.system("cls")
        currentTime += 0.5
        velocity = adjustVelocity(((currentBytesReceive - previousBytesReceive))/((currentTime - previousTime)/0.5))
        print "Velocity: %s" %(velocity)
        kByteReceive = (100*currentBytesReceive)/(totalBytes*1024.)
        print "Size: "+adjustSize(totalBytes)
        print "Bytes receive: "+ adjustSize(currentBytesReceive/1024.)
        print "Progress: %.2f%%" %(kByteReceive)
        drawProgress(kByteReceive)
        previousBytesReceive = currentBytesReceive
        previousTime = currentTime

def searchFile():
    global totalBytes
    s.connect((ipAddress, port))
    print filename
    s.send(filename)
    totalBytes = long(s.recv(buffer_size))/1024.

def getSizeFile():
    s.bind((ipAddress, port))
    s.listen(1)
    conn, addr = s.accept()
    data = s.recv(buffer_size)
    print "size "+data
    #conn.send("sizeReceived")
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




ipAddress = '127.0.0.1'
port = 4056
buffer_size = 1024

totalBytes = 0
currentBytesReceive = 0
previousBytesReceive = 0
currentTime = 0
previousTime = 0

filename = raw_input("filename: ")
totalBytesReceived = 0

searchFile()

fileTransferred = False
th = Thread( target=velocityCalculate, )

while (True):
    l = s.recv(buffer_size)
    if l == "":
        if (fileTransferred):
            print "Arquivo recebido."
            f.close()
        else:
            print "Arquivo nao encontrado."
        break
    if (not fileTransferred):
        th.start()
        f = open(filename+"_copia",'wb')
        fileTransferred = True
    while (l):
        f.write(l)
        l = s.recv(buffer_size)
        currentBytesReceive += 1024
s.close()