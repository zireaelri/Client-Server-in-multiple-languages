import socket			 

s = socket.socket()		 

port = 12345				

s.connect(('127.0.0.1', port)) 
s.send('Message from client'.encode())
print (s.recv(1024).decode()) 
s.close()	 
