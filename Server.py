import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(message)
        richiesta = message.split("|")
        idRichiesta = richiesta[0]
        if idRichiesta.equals("A"):
            accesso()
        elif  idRichiesta.equals("M"):
            messagio()
        else:
            break
        nome = richiesta[1]


            
async def main():
    async with websockets.serve(echo, "", 8765):
        await asyncio.Future()

asyncio.run(main())