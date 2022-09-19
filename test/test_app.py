import json
import pytest
from message_server.app import app, MESSAGES

@pytest.fixture
def client():
    return app.test_client()

def test_get_messages(client):
    MESSAGES['Val'].append({'fromUser': 'Steve', 'toUser': 'Val', 'message': 'Test Message'})
    response = client.get('/get-messages/Val')
    response_data = json.loads(response.data)
    assert response.status_code == 200
    assert len(response_data) == 1
    assert response_data[0]['toUser'] == 'Val'

def test_post_message(client):
    response = client.post(
        '/post-message',
        data=json.dumps({'fromUser': 'Val', 'toUser': 'Steve', 'message': 'Test Message'})
    )
    assert response.status_code == 202
    assert len(MESSAGES['Steve']) == 1
