import socket
c = socket.socket() #connecting two nodes on a network to communicate with each other
c.connect(('localhost' , 9999)) # localhost is a hostname that refers to the current computer used to access it.
# It is used to access the network services that are running on the host via the loopback network interface.
name=input("Enter the name : ")
c.send(bytes(name, 'utf-8')) #UTF-8 is one of the most commonly used encodings, and Python often defaults to using it.
# UTF stands for “Unicode Transformation Format”, and the '8' means that 8-bit values are used in the encoding. ...
# UTF-8 uses the following rules: If the code point is < 128, it's represented by the corresponding byte value.
print(c.recv(1024).decode())
c.close()