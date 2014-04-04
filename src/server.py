import socket
import os
import check

address = '127.0.0.1'
port = 4056
buffer_size = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while(1):
	try:
		s.bind((address, port))
		break 
	except: port += 1
s.listen(1)

while (1):
    print "\Waiting connection..."
    conn, addr = s.accept()
    print 'Address of connection', addr
    fileName = conn.recv(buffer_size)
    try:
        fileSize = str(os.path.getsize(fileName))
        fileSha1 = check.getSha1(fileName)
        conn.send("{\"size\":\""+fileSize+"\",\"sha1\":\""+fileSha1+"\"}")
        f = open (fileName, "rb") 
        
        print "Sending file: %s" % fileName
        l = f.read(buffer_size)    
        while(l):
            conn.send(l)
            l = f.read(buffer_size)
        f.close()
        print "File transferred."
    except IOError,e:
        print e
    finally:
        conn.close()
