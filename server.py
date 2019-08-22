import asyncio
import websockets

# Keeps track of active connections
connections = []


async def accept(socket, path):
    """ Called everytime a new client connects to the server """
    connections.append(socket)
    print('New connection, total', len(connections))

    try:
        while True:
            message = await socket.recv()
            await socket.send(message)
    except:
        # The socket raises an exception when the other side disconnects. Remove the connection
        connections.remove(socket)
        print('Disconnection, total', len(connections))

asyncio.get_event_loop().run_until_complete(websockets.serve(accept, "localhost", 8765))
asyncio.get_event_loop().run_forever()
