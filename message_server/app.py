# JSON is a lightweight format for storing and transporting data.
import json
# SQLite is a database that comes with Python
import sqlite3

# request is the way you access the incoming request
# Flask is what we'll use to create the actual app instance
from flask import request, Flask

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
    # establish a connection to the database
    conn = sqlite3.connect('messages.db')
    # create a cursor which we will use to execute sql
    cursor = conn.cursor()
    # list to hold all messages
    all_messages = []
    try:
        # execute sql to get messages for user
        result = cursor.execute(
            'SELECT * FROM messages WHERE to_user = ?',
            (user_id,)
        )
        # get column names from response
        column_names = [ descrip[0] for descrip in result.description ]
        # build dictionary response
        for msg in result.fetchall():
            all_messages.append(
                dict(
                    (column_names[i], msg[i]) for i in range(len(column_names))
                )
            )
    except Exception as e:
        print(e.message)
        return e.message, 500
    finally:
        cursor.close()
        conn.close()
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
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
          INSERT INTO messages (from_user, to_user, message)
          VALUES (?, ?, ?)
        ''', (message['fromUser'], message['toUser'], message['message'])
        )
        conn.commit()
    except Exception as e:
        print(e.message)
        return e.message, 500
    finally:
        cursor.close()
        conn.close()
    # return a nice response - for a comprehensive list of possible response codes,
    # see https://www.webfx.com/web-development/glossary/http-status-codes/
    return '', 202
