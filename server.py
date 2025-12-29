import socket 

s =  socket.socket()

print("Socket Created Succesfully ")

port = 1122

#can connect to any ip just listens for incoming req
s.bind(('',port)) 

print(f"Socket connected to {port}")

s.listen(5)

print("Socket is listening ")

while True: 
    c,addr = s.accept()
    print("Got the connection {addr}")

    c.send("Thanks for Connecting ")
    c.close()
