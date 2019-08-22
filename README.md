## Running Example# Asyncio Programming Challenge

This is a take-home programming challenge that's meant to test your ability to program (or learn to program)[asynchronously](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming). It uses `asyncio` to implement its concurrency. Put simply, asynchronous code is code that doesn't run top-to-bottom, start-to-finish, one line after another-- it runs out of order, with different sections logically executing at the same time. 

If you are new to `asyncio`, you may find the following links useful:

- [RealPython Walkthrough](https://realpython.com/async-io-python/)
- [Websockets Basic Example (used as the base for this test)](https://websockets.readthedocs.io/en/stable/intro.html)

Here is implemented a simple echo server using `websockets`, a library for exchanging string messages over a network. You could run this example over the internet if you wanted to, but for this challenge it's easier to just run both the server and the client locally on two terminals. 

## Running Example

You must have python3.6, websockets, and aioconsole installed. Python installation is not covered here. Install the others with:

```
sudo pip3 install websockets aioconsole
```

Then, open a terminal, navigate to this directory, and start the server:

```
python3 server.py
```

Open a second terminal, navigate to this directory, and start a client:

```
python3 client.py
```

Then type a sentence into the terminal thats running `client.py`, press Enter, and see that you got back an echoed copy of your message. It should look something like this:

```
python3 client.py
> Hello!
< Hello!
```


## Background

This section explains the basic concepts used in this challenge to keep this challenge from being about `asyncio` or `websockets` specifically. Skip down to the tasks section below if you want to get started. 

The first rule of `asyncio` is to never block with normal python code. "Blocking" means to stop execution at a section of code and not return. The following is a blocking section of code:

```
time.sleep(10)
```

So is:

```
while True:
	pass
```

Asyncio provides a mechanism for logically blocking with `async`/`await`. Functions marked with `async` **might** block. For example:

```
async def good_sleep():
	await asyncio.sleep(1)

...

await good_sleep()
```

Whenever you invoke an asynchronous function you must include the `await` in front of the function call, which waits for the asynchronous call to return. The difference between this and regular python blocking is that asyncio can run other tasks while one task is blocked. Note that `await` doesn't mean a function will logically block, just that it might. Only special I/O calls actually block. All the calls in this demo that block are shown below:

```
await websockets.connect("")
await socket.send("message")
message = await socket.recv()

await asyncio.sleep(0.1)
```

Websockets is a networking protocol that exchanges string messages one at at time. Picture a socket as a pipe that both the client and the server hold. When one side calls `send` and passes a string, it appears on the other side which calls `recv` (or receive) to pick it up. These calls block because send takes time to write something to the network, and receive will wait until there's a message to return it.

When these calls are awaited, other tasks can run. Line 13 of client.py demonstrates how to make a new task:

```
asyncio.get_event_loop().create_task(print_results(socket))
```

Making a new task means peeling off a new logical point of execution. In other words, it makes your code run in more than one place. Creating a task does not block-- it starts the new task in its own time. 

Note that `server.py` automatically creates a new task every time a client connects and `accept` is called. 

## Tasks

These challenges scale in difficulty, and you are not meant to solve them all. Each step is meant to test your understanding of concurrent execution, not Python, networking, or websockets. You can solve each of these with only the imports present in the base example, but feel free to use whatever libraries or resources you want. Don't use `threading` or `multiprocessing`, though, thats cheating.

You do not need to use any other parts of the `asyncio` module to complete this challenge. The solutions to these tasks can be implemented in a few lines apiece. The function calls and code patterns needed to complete these tasks have largely already been used once. 

Do not modify the client in any task, but do read it over and try to understand it-- the code there will be helpful in solving some of these tasks. 

### Task 1: Chatroom

You can connect more than one client to the echoserver at once, but each client will only hear back their own echo. Convert the echo server to a chatroom, so two seperate terminals connected as clients can send messages back and forth. When you connect two clients to a single server and type into one of the clients, you should see your message in the other client. 

### Task 2: Timestamps

Add timestamps on messages from other users that show the number of seconds that have elapsed since *that user* connected. 

For example, when one client connects, then three seconds later sends a message `pizza later?`, waits 3 seconds, then `or maybe pasta` the other client should see:

```
< 3 pizza later? 
< 6 or maybe pasta?
```

The `3` indicates the first message arrived 3 seconds after that client connected. 

### Task 3: Pagers

Add a feature in the server to page users to get their attention. If any client sends the text string `page` to the server, the server should send `PAGING` to every connected client once a second until *another* client types anything-- not the original client. The client who sent the page must still be able to send normal chat messages while a page is active, and they should not see the `PAGING` alert printed in their chat window. 

### Task 4: Private Chat

Add a private chat feature that lets two users enter a private chat in such a way that they only see each other's messages, and no other connected client can see their messages. First, add names to clients and broadcast their name to the chatroom when they connect. Then create a command `invite <name>` in the server that will move another user to a private chat and tell them who they're chatting with. Users should be able to leave a chat with `leave`. If either user disconnects from the server, the other user should be dropped back into the regular chatroom. 

For example, if client 1 connects before client 2, client 1 should see:

```
< Client 2 connected
```

Then if client 1 types `invite 1` into the chat, client 2 should see:

```
Private chatting with Client 1
```

and client 1 should see:

```
Private chatting with Client 2
```

If client 2 types `leave`, client 1 should see:

```
Private chat ended.
```


### Tricky Questions

These are tricky questions and not part of the challenge, but if you understand asyncio very well you should be able to answer them. 

- How many clients can connect at once? 

You must have python3.6 and websockets installed. Python installation is not covered here. Install websockets with:

```
sudo pip3 install websockets
```

Then, open a terminal, navigate to this directory, and start the server:

```
python3 server.py
```

Open a second terminal, navigate to this directory, and start a client:

```
python3 client.py
```

Then type a sentence into the terminal thats running `client.py`, press Enter, and see that you got back an echoed copy of your message. It should look something like this:

```
python3 client.py
> Hello!
< Hello!
```


## Background

This section explains the basic concepts used in this challenge to keep this challenge from being about `asyncio` or `websockets` specifically. Skip down to the tasks section below if you want to get started. 

The first rule of `asyncio` is to never block with normal python code. "Blocking" means to stop execution at a section of code and not return. The following is a blocking section of code:

```
time.sleep(10)
```

So is:

```
while True:
	pass
```

Asyncio provides a mechanism for logically blocking with `async`/`await`. Functions marked with `async` **might** block. For example:

```
async def good_sleep():
	await asyncio.sleep(1)

...

await good_sleep()
```

Whenever you invoke an asynchronous function you must include the `await` in front of the function call, which waits for the asynchronous call to return. The difference between this and regular python blocking is that asyncio can run other tasks while one task is blocked. Note that `await` doesn't mean a function will logically block, just that it might. Only special I/O calls actually block. All the calls in this demo that block are shown below:

```
await websockets.connect("")
await socket.send("message")
message = await socket.recv()

# This one isn't used in the demo. It casues asyncio to wait for 1 second.
await asyncio.sleep(1)
```

Websockets is a networking protocol that exchanges string messages one at at time. Picture a socket as a pipe that both the client and the server hold. When one side calls `send` and passes a string, it appears on the other side which calls `recv` (or receive) to pick it up. These calls block because send takes time to write something to the network, and receive will wait until there's a message to return it.

When these calls are awaited, other tasks can run. Line 13 of client.py demonstrates how to make a new task:

```
asyncio.get_event_loop().create_task(print_results(socket))
```

Making a new task means peeling off a new logical point of execution. In other words, it makes your code run in more than one place. Creating a task does not block-- it starts the new task in its own time. 

Note that `server.py` automatically creates a new task every time a client connects and `accept` is called. 

## Tasks

These challenges scale in difficulty, and you are not meant to solve them all. Each step is meant to test your understanding of concurrent execution, not Python, networking, or websockets. You can solve each of these with only the imports present in the base example, but feel free to use whatever libraries or resources you want. Don't use `threading` or `multiprocessing`, though, thats cheating.

You do not need to use any other parts of the `asyncio` module to complete this challenge. The solutions to these tasks can be implemented in a few lines apiece. The function calls and code patterns needed to complete these tasks have largely already been used once. 

Do not modify the client in any task, but do read it over and try to understand it-- the code there will be helpful in solving some of these tasks. 

### Task 1: Chatroom

You can connect more than one client to the echoserver at once, but each client will only hear back their own echo. Convert the echo server to a chatroom, so two seperate terminals connected as clients can send messages back and forth. When you connect two clients to a single server and type into one of the clients, you should see your message in the other client. 

### Task 2: Timestamps

Add timestamps on messages from other users that show the number of seconds that have elapsed since *that user* connected. 

For example, when one client connects, then three seconds later sends a message `pizza later?`, waits 3 seconds, then `or maybe pasta` the other client should see:

```
3 < pizza later? 
6 < or maybe pasta?
```

The `3` indicates the first message arrived 3 seconds after that client connected. 

### Task 3: Pagers

Add a feature in the server to page users to get their attention. If any client sends the text string `page` to the server, the server should send `PAGING` to every connected client once a second until *another* client types anything-- not the original client. The client who sent the page must still be able to send normal chat messages while a page is active, and they should not see the `PAGING` alert printed in their chat window. 

### Task 4: Private Chat

Add a private chat feature that lets two users enter a private chat in such a way that they only see each other's messages, and no other connected client can see their messages. The "name" associated with each user should be some number that doesn't conflict with any other user's ID and stays fixed while the user is connected. If that client disconnects and reconnects, they should get a new ID thats never been used. Then create a command `invite <name>` in the server that will move another user to a private chat and tell them who they're chatting with. Users should be able to leave a chat with `leave`. If either user disconnects from the server, the other user should be dropped back into the regular chatroom. 

For example, if client 1 connects before client 2, client 1 should see:

```
< Client 2 connected
```

Then if client 1 types `invite 1` into the chat, client 2 should see:

```
Private chatting with Client 1
```

and client 1 should see:

```
Private chatting with Client 2
```

If client 2 types `leave`, client 1 should see:

```
Private chat ended.
```


