# JSON is a lightweight format for storing and transporting data.
import json

# request is the way you access the incoming request
# Flask is what we'll use to create the actual app instance
from flask import request, Flask

# defaultdict is a really handy convenience tool that allows you to
# create a python dictionary that will have default values when you access a key
# In this case, if I request a key that doesn't exist, it will return an empty array.
# For more info, see https://realpython.com/python-defaultdict/
from collections import defaultdict

# Creating the Flask APP. `__name__` is a variable that is accessible to all python modules
# and isn't particularly relevant at the moment
app = Flask(__name__)

# Creating my storage. Note this will be empty every time I start the server. It would
# be better to use a more permanent storage mechanism.
MESSAGES=defaultdict(list)

# This is a "decorator" (see https://realpython.com/primer-on-python-decorators/).
# It tells the app we created above that when a request is received for this "path",
# respond by using this function. It also contains a variable "user_id", which gets passed
# into the function. For example, if someone requests /get-messages/Val, "Val" will be passed
# in on the `user_id` variable to the function.
@app.route('/get-messages/<user_id>')
def get_messages(user_id):
    # get messages from our storage variable for the given "user_id"
    all_messages = MESSAGES.get(user_id, [])
    # return the messages in a JSON format
    return json.dumps(all_messages)


# Decorator to handle routing for posting messages. "methods" here specifies
# what http method this route accepts. We can get into that more later
@app.route('/post-message', methods=['POST'])
def post_message():
    '''
    convert the incoming message from JSON format to a python dictionary
    the message is expected to be a dictionary that looks like this:
       {
         "fromUser": the user id sending the message,
         "toUser": the user id receiving the message,
         "message": the text of the message
       }
    '''
    message = json.loads(request.data)
    # write to the MESSAGES storage variable using the "toUser" value from the message as the key
    MESSAGES[message['toUser']].append(message)
    # return a nice response - for a comprehensive list of possible response codes,
    # see https://www.webfx.com/web-development/glossary/http-status-codes/
    return '', 202
