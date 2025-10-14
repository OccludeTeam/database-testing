import asyncio
import websockets

async def connect_to_websocket():
    uri = "wss://xaurbfygscqijzbhagcn.supabase.co/functions/v1/websocket-server"

    try:
        async with websockets.connect(uri) as websocket:
            print("i lowk feel the connection with bro")

            welcome_message = await websocket.recv()
            print(f"Server says: {welcome_message}")

            await websocket.send("can a homie get the time around here?")
            print("Sent: can a homie get the time around here?")

            response = await websocket.recv()
            print(f"Server sent back: {response}")

    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    asyncio.run(connect_to_websocket())