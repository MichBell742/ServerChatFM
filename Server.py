import asyncio
import websockets
import websockets.exceptions as exc
import funzioni as utility
import user 

utentiOnline = []

async def echo(websocket):
    global utentiOnline
    print(type(websocket))
    try:
        async for message in websocket:
            print(message)
            richiesta = message.split("|")
            idRichiesta = richiesta[0]
            if idRichiesta=='A':
                if utility.accesso(richiesta):
                    if not loggato(richiesta[1]):
                        utente = user.User(websocket,richiesta[1])
                        utentiOnline.append(utente)
                        await utente.getWebsocket().send("R|ok")
                        await utility.sendOnlineUsers(utentiOnline)
                    else:
                        print("è gia loggato sto pirlone")
                        break
                else:
                    await websocket.send("R|no")
            elif  idRichiesta=='M':
                if utility.messaggio(richiesta):
                    await utility.sendBroadcast(utentiOnline, message)
                else:
                    print("errore nel messaggio")
            else:
                print("non coerente")   
                break
        utentiOnline=utility.deleteByWebSocket(utentiOnline, websocket)
        await utility.sendOnlineUsers(utentiOnline)
    except exc.ConnectionClosedError: 
        print("disconnected Errore")
    except exc.ConnectionClosedOK: 
        print("disconnected ok")
    except exc.ConnectionClosed:
        print("disconnected")

def loggato(nome):
    for user in utentiOnline:
        if user.getNome()==nome:
            return True
    return False

async def main():
    async with websockets.serve(echo, "", 8765):
        await asyncio.Future()

asyncio.run(main())