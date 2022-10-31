# JSON is a lightweight format for storing and transporting data.
import json

# request is the way you access the incoming request
# Flask is what we'll use to create the actual app instance
from flask import request, Flask

# importing models to use the objects there
from message_server.models import User, Message

# Creating the Flask APP. `__name__` is a variable that is accessible to all python modules
# and isn't particularly relevant at the moment
app = Flask(__name__)

# This is a "decorator" (see https://realpython.com/primer-on-python-decorators/).
# It tells the app we created above that when a request is received for this "path",
# respond by using this function. It also contains a variable "user_id", which gets passed
# into the function. For example, if someone requests /get-messages/Val, "Val" will be passed
# in on the `user_id` variable to the function.
@app.route('/get-messages/<user_id>')
def get_messages(user_id):
    # list to hold all messages
    all_messages = []
    try:
        for message in Message.get(to_user_id=user_id):
            all_messages.append(message.to_json())
    except Exception as e:
        print(e.message)
        return e.message, 500
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
    request_data = json.loads(request.data)
    message = Message(
        from_user_id=request_data['fromUser'],
        to_user_id=request_data['toUser'],
        message=request_data['message']
    )
    message.save()
    return '', 202
