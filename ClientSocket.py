def ConectaCliente():
    import socket
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('127.0.0.1',8080))
    message = f"Mensagem recebida pelo Cliente"
    client.send(message.encode('utf-8'))
    from_server = client.recv(4096)
    client.close()
    print(from_server.decode())
