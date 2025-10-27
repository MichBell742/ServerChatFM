import asyncio
import websockets
import websockets.exceptions as exc
import metodi as utility
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
                        await utente.getWebsocket().send("U|ok")
                    else:
                        print("è gia loggato sto pirlone")
                        break
                else:
                    await websocket.send("U|no")
            elif  idRichiesta=='M':
                for client in utentiOnline:
                    await client.getWebsocket().send(message)
            else:
                print("non coerente")   
                break
    except exc.ConnectionClosedError: 
        utentiOnline=utility.deleteByWebSocket(utentiOnline, websocket)
        print("disconnected Errore")
    except exc.ConnectionClosedOK: 
        utentiOnline=utility.deleteByWebSocket(utentiOnline, websocket)
        print("disconnected ok")


def loggato(nome):
    for user in utentiOnline:
        if user.getNome()==nome:
            return True
    return False





async def main():
    async with websockets.serve(echo, "", 8765):
        await asyncio.Future()

asyncio.run(main())