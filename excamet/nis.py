import asyncio
import websockets

async def send_message(uri, message):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        print(f"Sent: {message}")
        
        # Optionally, you can receive a response from the server
        response = await websocket.recv()
        print(f"Received: {response}")

# Example usage
uri = "ws://your-websocket-server-uri"
message = "Hello, WebSocket!"

# Running the async function using asyncio
asyncio.run(send_message(uri, message))
