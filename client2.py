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
        recv_message = s.recv(1024)
        recv_message = recv_message.decode()
        print("Mensagem recebida : ", recv_message)
        