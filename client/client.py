import socket
import sys

IP=sys.argv[1]

HOST = IP  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

with open('video.mp4', 'rb') as arquivo:
    dados = arquivo.read()
    tcp.sendall(dados)

tcp.close()

