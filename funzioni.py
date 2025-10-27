import csv
def messaggio():
    return "interpreto messaggio"

def accesso(richiesta):
    nome = richiesta[1]
    psw = richiesta[2]
    verifica = False
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
