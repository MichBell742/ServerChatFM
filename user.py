class User:
    def __init__(self, websocket, nome):
        self.websocket = websocket
        self.nome = nome
    
    def getWebsocket(self):
        return self.websocket
    
    def getNome(self):
        return self.nome