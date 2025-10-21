import asyncio
import websockets
import metodi as utility

async def echo(websocket):
    print(type(websocket))
    async for message in websocket:
        print(message)
        richiesta = message.split("|")
        idRichiesta = richiesta[0]
        if idRichiesta=='A':
            print(utility.accesso())
        elif  idRichiesta=='M':
            print(utility.messaggio())
        else:
            break
    
async def main():
    async with websockets.serve(echo, "", 8765):
        await asyncio.Future()

asyncio.run(main())