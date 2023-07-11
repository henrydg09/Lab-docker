# Alunos: Henry Duarte e Julia Mendes

# Lab-docker

Primeiramente vamos escrever os comandos para utilizar o servidor em uma máquina qualquer

```
docker run -it --rm --network=host henrydg/server:v2 /bin/bash
```
No terminal do container ultilizar o seguinte comando:
```
python3 server.py
```
Desse modo o servidor fica aguardando os arquivos do cliente


Posteriormente, em outra máquina vamos escrever os comandos para utilizar o cliente
```
sudo docker run -it --rm --network=host henrydg/client:v2 python3 client.py  <IP SERVIDOR>
```
Retirar os <> e passar o endereço ip. Vai ser solicitado o nome do arquivo que se deseja enviar: video.mp4 ou texto.txt.
Após isso deve-se digitar o nome do arquivo na máquina do servidor que deseja salvar.

E por fim, executar o comando Ctrl+C no servidor e visualize o arquivo enviado.



