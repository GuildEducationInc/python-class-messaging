# python-class-messaging

This repository contains very basic code for the Python class. It's a messaging application that allows the user to send and receive messages. It uses flask as the web framework and a (not-recommended) in-memory database for storage.

Prerequisites:
- Python3.9 at a minimum
- Virtual environment created and requirements installed
  - `python3 -m venv venv`
  - `. venv/bin/activate`
  - `pip install -r requirements.txt`
  
To run (with activated virtual environment):
`FLASK_APP=message_server flask run`
