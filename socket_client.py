import socket
import json

# create a object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define the port on which server is running
port = 80

# connect to the server
s.connect(('0.0.0.0', port))

while True:
    message = str(input("enter your message: "))

    # send to server
    data = {
        "route": "stream",
        "message": message,
        "more": "this is message from socket client"
    }
    data = json.dumps(data)
    s.send(data.encode())

    # receive data from server
    print(s.recv(4096))

# close the connection
s.close()
