import socket
s = socket.socket()
host = socket.gethostname()
port = 6789
s.connect((host, port))
print("Conectado ao servidor")
message = s.recv(1024)
message = message.decode()
print("Mensagem do servidor: ", message)


while 1:
        message = input(str(">>"))
        message = message.encode()
        s.send(message)
        print("Mensagem enviada")


