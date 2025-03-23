# Python Socket Client-Server Chat

This is a simple Python project showing how to send messages between a client and a server using TCP sockets.

-------------------------------------
📁 Files:

- server.py → Listens for connections and handles multiple clients using threads.
- client.py → Connects to the server and sends messages.

-------------------------------------
⚙️ How It Works:

- The client sends a message with a fixed-length header (64 bytes) that tells the server how long the message is.
- The server reads the header, then the message, and replies with "message received".
- To disconnect, the client sends: DISCONNECTED!

-------------------------------------
▶️ How to Run:

1. Start the server:
   python server.py

2. Run the client (in another terminal or computer):
   python client.py

-------------------------------------
✅ Features:

- Multiple client support (using threading)
- Fixed-length message header
- Clean disconnect handling

-------------------------------------
📌 Notes:

- Change the IP in client.py to match your network/server IP.
- No external libraries required.

-------------------------------------
🧰 Requirements:

- Python 3.x

-------------------------------------
🪪 License:

MIT License – Free to use and modify.
