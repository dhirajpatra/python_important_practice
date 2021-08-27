import socket

# server socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 80
# binding to start server
serv.bind(('0.0.0.0', port))
serv.listen(5)

print("Server started and listing for client connections on port %s" % port)

# true for indefinite
while True:
    conn, addr = serv.accept()
    from_client = ''

    while True:
        data = conn.recv(4096)
        if not data:
            break
        from_client += data.decode()

        response = "welcome " + from_client
        conn.send(response.encode())
        print(from_client)

    conn.close()

    print('client disconnected')
