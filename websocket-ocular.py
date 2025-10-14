import asyncio
import websockets

async def connect_to_websocket():
    # Construct the correct WebSocket URL for your Supabase Edge Function.
    # It must start with 'wss' and point directly to your function's path.
    uri = "wss://xaurbfygscqijzbhagcn.supabase.co/functions/v1/websocket-server"

    try:
        async with websockets.connect(uri) as websocket:
            print("i lowk feel the connection with bro")

            # Listen for the welcome message from the server
            welcome_message = await websocket.recv()
            print(f"Server says: {welcome_message}")

            # Send a message to the server
            await websocket.send("can a homie get the time around here?")
            print("Sent: can a homie get the time around here?")

            # Listen for the server's response
            response = await websocket.recv()
            print(f"Server sent back: {response}")

    except Exception as e:
        print(f"Connection failed: {e}")

# Run the client
if __name__ == "__main__":
    asyncio.run(connect_to_websocket())