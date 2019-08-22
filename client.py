import asyncio
import websockets
import aioconsole


async def print_results(socket):
    while True:
        response = await socket.recv()
        print(f"< {response}")


async def chat():
    socket = await websockets.connect('ws://localhost:8765')
    asyncio.get_event_loop().create_task(print_results(socket))

    # Wait for user keyboard input, send it to the chat, and print the response
    while True:
        message = await aioconsole.ainput('> ')
        await socket.send(message)
        await asyncio.sleep(0.1)

asyncio.get_event_loop().run_until_complete(chat())

