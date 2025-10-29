import csv
def messaggio(richiesta,utentiOnline):
    try:
        nome = richiesta[1]
        for i in utentiOnline:
            if nome != i.getNome():
                presente = False
            else:
                presente= True
        if not presente:
            return False
        ora= richiesta[2]
        paese = richiesta[3]
        mediaType = richiesta[4]
        media = richiesta[5]
        return True
    except IndexError:
        return False

def accesso(richiesta, websocket, utenti):
    websocketNonPresente=True
    for user in utenti:
        #verifico che non il webSocket non sia già esistente evitando l'accesso dallo stesso client
        if(user.getWebsocket()==websocket):
            websocketNonPresente=False
            break
    verifica = False
    if websocketNonPresente:
        nome = richiesta[1]
        psw = richiesta[2]
        with open('log.csv', mode='r', newline='', encoding='utf-8') as file:
            lettore = csv.reader(file, delimiter=',')
            for riga in lettore:
                print(riga)
                if riga[0]==nome and riga[1]==psw :
                    #print("coretto")
                    verifica = True
                    break
    return verifica

def deleteByWebSocket(users, websocket):
    for user in users:
        if user.getWebsocket() == websocket:
            users.remove(user)
            print(user.getNome() + " si è disconnesso")
    return users

async def sendOnlineUsers(utenti):
    message="U|"
    for i in range(len(utenti)):
        if not i==0:
            message+="|"+utenti[i].getNome()
        else:
            message+=utenti[i].getNome()
    await sendBroadcast(utenti, message)

async def sendBroadcast(utenti, message):
    for client in utenti:
        await client.getWebsocket().send(message)