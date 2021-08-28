import socket
s=socket.socket()
print('socket created')
s.bind(('localhost', 9999))
s.listen(3)
print('waiting for the connections')
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connnected with" , addr , name)
    c.send(bytes('welcome, Its Parth Sharma' ,'utf-8'))
    c.close()