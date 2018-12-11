#!/usr/bin/python3
import socket
import requests

# On créé le serveur qui écoute sur le port 17
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 17))
server.listen(5)

print("Server listening on port 17")
#On écoute sans cesse
while True:
    sock, addr = server.accept()
    print("Connection opened from {}:{}".format(sock.getpeername()[0],sock.getpeername()[1]))
    #On va chercher la quote à renvoyer par l'api
    r = requests.get("https://api.chucknorris.io/jokes/random")
    quote=r.json()["value"] + "\n"
    #On envoie la quote
    sock.send(bytes(quote, "UTF-8"))
    print("Answer sent")
    sock.close()
    print("Connection closed")

