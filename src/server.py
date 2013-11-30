import socket
import os

address = '127.0.0.1'
port = 4056
buffer_size = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((address, port))
s.listen(1)

while (1):
    print "\Waiting connection..."
    conn, addr = s.accept()
    print 'Address of connection', addr
    nomeDoArquivo = conn.recv(buffer_size)
    try:
        conn.send(str(os.path.getsize(nomeDoArquivo)))
        f = open (nomeDoArquivo, "rb") 
        
        print "Sending file: %s" % nomeDoArquivo
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