import json

from flask import request, Flask

from collections import defaultdict
app = Flask(__name__)
MESSAGES=defaultdict(list)

@app.route('/get-messages/<user_id>')
def get_messages(user_id):
    all_messages = MESSAGES.get(user_id, [])
    return json.dumps(all_messages)


@app.route('/post-message', methods=['POST'])
def post_message():
    message = json.loads(request.data)
    MESSAGES[message['toUser']].append(message)
    return '', 202
