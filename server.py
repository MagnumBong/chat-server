#libraries
import json
import asyncio

#main
class Server:

    def __init__(self):
        self.login_data = json.load(open('./data/login.json'))

    async def net_startup():
        print("Starting websocket...")
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "178.128.160.116"
        port = 8000
        time.sleep(2)
        serversocket.bind((host, port))
        print("Binding to port...")
        serversocket.listen(5)
        while 1:
            (clientsocket, address) = serversocket.accept()
            data = clientsocket.recv(1024).decode()
            print (data)
            r='REceieve'
            clientsocket.send(r.encode())

    async def authenticate_login(self):
        pass

Server().net_startup()
