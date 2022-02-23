def StartServer():
    import socket

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('127.0.0.1',8080))
    serv.listen(5)
    while True:
        conn, addr = serv.accept()
        from_client = ''
        while True:
            data = conn.recv(4096)
            if not data: break
            from_client += str(data.decode())
            print(from_client)
            message = f"I am Server, connected by {addr} "
            conn.send(message.encode('utf-8'))
        conn.close()
        print('Client disconnected')
