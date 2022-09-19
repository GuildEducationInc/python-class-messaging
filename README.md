# python-class-messaging

This repository contains very basic code for the Python class. It's a messaging API that allows the user to send and receive messages. It uses [Flask](https://flask.palletsprojects.com/en/2.2.x/) as the web framework and a (not-recommended) in-memory database for storage. This is the take-home project we send to prospective engineers.

The API runs in a web server on your local machine. You can hit that web server with a browser, but for a little more capability (and because this is a python class), we'll be using a python library called `requests` to interact with the web server.

There are two "endpoints" to this api:
- `/get-messages/<user id>` This endpoint will retrieve all messages for the given user id, so for example your request might look like `http://localhost:8080/get-messages/Val` to get all messages for "Val".
- `/post-message` This endpoint is how put put new messages into the system. You'll send data along with that request to tell the system what to store.

All of the commands here need to be run on the command line. The instructions here are for Mac OS. I'll need help to figure out what they should be on Windows. I recommend using [iTerm](https://iterm2.com) on a Mac, but it's not strictly necessary.

### Prerequisites:
- Python3.9 at a minimum
- Virtual environment created and requirements installed
  - `python3 -m venv venv` (This creates a copy of python in a directory called `venv` where you can install libraries without messing with the system-level libraries. Think of it as a temporary python install. If you ever need to reset everything, just delete the directory and reinstall with this command.)
  - `. venv/bin/activate` (This "turns on" that temporary python. To turn it back off again, run `deactivate`).
  - `pip install -r requirements.txt` (This installs the necessary libraries to run this code - specifically Flask and requests)
  
### To run the server:
`FLASK_APP=message_server flask run -h localhost -p 8080` (this tells flask to use the code in `message_server` as its application code and also says to respond on `localhost` which is your local machine and on port 8080)

To interact with the server, we're using a library called `requests` which is installed with the `pip install` command in the prerequisites. It allows you to make web requests to a web server programatically. You should run the server in one window and then open a new window, go to the directory you've got the code in, activate your virtual environment (`. venv/bin/activate`), then run python in interactive mode: `python`.

There is a lot around Flask I'm currently not going over (especially what the `@app.route` stuff is in the code). Effectively, those lines of code just tell Flask how to route the request. We can cover in more detail another time.

### Set up to interact with API
- Switch to the directory where you pulled the code
- Activate the virtual environment `. venv/bin/activate`
- Start python `python`
- Import the requests library - `import requests`

### Send a message
- `requests.post('http://localhost:8080/post-message', data='{"fromUser": "From", "toUser": "To", "message": "Very first message"}')
There's a bit to go through here:
- `requests.post` is making a "POST" request to your server. We'll go into a little more detail later on what that means.
- `/post-message` tells Flask where to go with your request - in this case, the `post_message` function in `message_server/__init__.py`
- `data={...}` is the data to send in your request. It's effectively sending a message that contains a "fromUser" - "From", a "toUser" - "To", and a text "message". Feel free to play around with these values. I will note, however, that changing or removing "toUser" will cause issues.

### Get messages
- `requests.get('http://localhost:8080/get-messages/To')`
Here's what this is saying:
- `requests.get` is making a "GET" request to your server.
- `get-messages` tells Flask where to go with your request - in this case, the `get_messages` function in `message_server/__init__.py`
- `To` is the "toUser" specified in the message that was posted earlier
