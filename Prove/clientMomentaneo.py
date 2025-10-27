import asyncio
import websockets

async def hello():
    uri = "ws://192.168.1.33:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            try:
                msg=input("cosa vuoi scrivere: ")
                await websocket.send(msg)
                response = await websocket.recv()
                print("Risposta: {response}")
            except websockets.exceptions.ConnectionClosedError:
                print("Disconnessione ERRORE")
                break
            except websockets.exceptions.ConnectionClosedOK:
                print("Disconnession OK")
                break
    


asyncio.run(hello())
