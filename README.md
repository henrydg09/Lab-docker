# Alunos: Henry Duarte e Julia Mendes

# Lab-docker

Primeiramente vamos escrever os comandos para utilizar o servidor em uma máquina qualquer

```
docker run -it --rm --network=host henrydg/server:v1 /bin/bash
```
No terminal do container ultilizar o seguinte comando:
```
python3 server.py
```
Desse modo o servidor fica aguardando os arquivos do cliente


Posteriormente, em outra máquina vamos escrever os comandos para utilizar o cliente
```
sudo docker run -it --rm --network=host henrydg/client:v1 python3 client.py  <IP SERVIDOR>
```
Retirar os <> e passar o endereço ip

E por fim, executar o comando Ctrl+C no servidor e visualize o arquivo enviado chamado de video.mp4 .



