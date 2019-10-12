import socket			 

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print "Socket successfully created"
except socket.error as err: 
    print "socket creation failed with error %s" %(err) 

port = 12345				

s.bind(('', port))		 
print "socket binded to %s" %(port) 

s.listen(5)	 
print "socket is listening"			

while True: 

    c, addr = s.accept()	 
    print 'Got connection from', addr 

    c.send('Thank you for connecting') 

    c.close() 
