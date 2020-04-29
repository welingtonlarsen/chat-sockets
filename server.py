import socket

serverSocket = socket.socket()
host = socket.gethostname()
port = 6789
serverSocket.bind((host, port))
serverSocket.listen(1)

print("O servidor esta aguardando os dois clientes")
primeiraConexao, primeiroEndereco = serverSocket.accept()
print("Primeiro cliente foi conectado...")
primeiraConexao.send("Bem vindo ao servidor, voce é o cliente 1 (que envia a mensagem)".encode())
print("Aguardando pela segunda conexão")
segundaConexao, segundoEndereco = serverSocket.accept()
print("Segundo cliente foi conectado...")
segundaConexao.send("Bem vindo ao servidor, você é o cliente 2 (que recebe a mensagem)".encode())

while 1:
        recv_message = primeiraConexao.recv(1024)
        segundaConexao.send(recv_message)
        print("Mensagem enviada do cliente 1 ao cliente 2")

