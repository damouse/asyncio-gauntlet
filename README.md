# Asyncio Programming Challenge

This is a take-home programming challenge that's meant to test your ability to program (or learn to program)[asynchronously](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming). It uses `asyncio` to implement its concurrency. Put simply, asynchronous code is code that doesn't run top-to-bottom, start-to-finish, one line after another-- it runs out of order, with different sections logically executing at the same time. 

If you are new to `asyncio`, you may find the following links useful:

- [RealPython Walkthrough](https://realpython.com/async-io-python/)
- [Websockets Basic Example (used as the base for this test)](https://websockets.readthedocs.io/en/stable/intro.html)

Here is implemented a simple echo server using `websockets`, a library for exchanging string messages over a network. You could run this example over the internet if you wanted to, but for this challenge it's easier to just run both the server and the client locally on two terminals. 

## Running Example

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

Some background on asyncio: async/await, create_task. 

## Challenge

These challenges scale in difficulty, and you are not meant to solve them all. Each step is meant to test your understanding of concurrent execution, not Python, networking, or websockets. You can solve each of these with only the imports present in the base example, but feel free to use whatever libraries or resources you want. Don't use `threading` or `multiprocessing`, though, thats cheating.

You do not need to use any other parts of the `asyncio` module to complete this challenge. The solutions to these tasks can be implemented in a few lines apiece.

### Task 1: Chatroom

You can connect more than one client to the echoserver at once, but each client will only hear back their own echo. Convert the echo server to a chatroom, so two seperate terminals connected as clients can send messages back and forth. When you connect two clients to a single server and type into one of the clients, you should see your message in the other client. 

Do not modify the client.

### Task 2: Timestamps

Add a timestamp feature so each client can see how long its been since *that user* connected. Use `round(time.time())`, which returns Unix time in seconds, as a source of time. The `round()` call just gets rid of the decimal values. Don't forget to `import time`.

For example, when one client connects, then three seconds later sends a message `pizza later?`, waits 3 seconds, then `or maybe pasta` the other client should see:

```
3 < pizza later? 
6 < or maybe pasta?
```

Do not modify the client.

### Task 3: Round-Trip Timestamps


