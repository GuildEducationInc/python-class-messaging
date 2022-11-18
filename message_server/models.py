import sqlite3

class User():

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.last_name = kwargs.get('last_name')
        self.first_name = kwargs.get('first_name')

    def save(self):
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        try:
            if self.id:
                cursor.execute(
                    'UPDATE users SET last_name=?, first_name=?, WHERE id=?',
                    (self.last_name, self.first_name, self.id)
                )
            else:
                cursor.execute(
                    'INSERT INTO users (last_name, first_name) VALUES (?, ?)',
                    (self.last_name, self.first_name)
                )
                self.id = cursor.lastrowid
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def to_json(self):
        return {
            'id': self.id,
            'last_name': self.last_name,
            'first_name': self.first_name,
        }

    @staticmethod
    def get(user_id=None, last_name=None, first_name=None, order_by=None):
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        sql = 'SELECT id, last_name, first_name FROM users WHERE 1 = 1'
        params = []
        if user_id:
            sql += ' AND id = ?'
            params.append(user_id)
        if last_name:
            sql += ' AND LOWER(last_name) like ?'
            params.append(f'%{last_name}%')
        if first_name:
            sql += ' AND LOWER(first_name) like ?'
            params.append(f'%{first_name}%')
        result = cursor.execute(sql, params)
        response = []
        for user in result.fetchall():
            response.append(User(id=user[0], last_name=user[1], first_name=user[2]))

        return response


class Message():

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.from_user_id  = kwargs.get('from_user_id')
        self.to_user_id  = kwargs.get('to_user_id')
        self.message = kwargs.get('message')

    def save(self):
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        try:
            if self.id:
                cursor.execute(
                    'UPDATE messages SET message=?, to_user_id=?, from_user_id=? WHERE id=?',
                    (self.message, self.to_user_id, self.from_user_id, self.id)
                )
            else:
                cursor.execute(
                    'INSERT INTO messages (from_user_id, to_user_id, message) VALUES (?,?,?)',
                    (self.from_user_id, self.to_user_id, self.message)
                )
                self.id = cursor.lastrowid
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def to_json(self):
        return {
            'id': self.id,
            'to_user_id': self.to_user_id,
            'from_user_id': self.from_user_id,
            'message': self.message
        }

    @staticmethod
    def get(message_id=None, from_user_id=None, to_user_id=None, order_by=None):
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        sql = 'SELECT id, from_user_id, to_user_id, message FROM messages WHERE 1 = 1'
        params = []
        if message_id:
            sql += ' AND id = ?'
            params.append(message_id)
        if from_user_id:
            sql += ' AND from_user_id = ?'
            params.append(from_user_id)
        if to_user_id:
            sql += ' AND to_user_id = ?'
            params.append(to_user_id)
        result = cursor.execute(sql, params)
        response = []
        for message in result.fetchall():
            response.append(
                Message(
                    id=message[0],
                    from_user_id=message[1],
                    to_user_id=message[2],
                    message=message[3]
                )
            )

        return response


class Comment():

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.user_id  = kwargs.get('user_id')
        self.message_id  = kwargs.get('message_id')
        self.comment = kwargs.get('comment')

    def save(self):
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        try:
            if self.id:
                cursor.execute(
                    'UPDATE comments SET comment=?, user_id=?, message_id=? WHERE id=?',
                    (self.comment, self.user_id, self.message_id, self.id)
                )
            else:
                cursor.execute(
                    'INSERT INTO comments (user_id, message_id, comment) VALUES (?,?,?)',
                    (self.user_id, self.message_id, self.comment)
                )
                self.id = cursor.lastrowid
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'message_id': self.message_id,
            'comment': self.comment
        }
    @staticmethod
    def get(message_id=None, comment=None, user_id=None, order_by=None):
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        sql = 'SELECT id, user_id, message_id, comment FROM comments WHERE 1 = 1'
        params = []
        if message_id:
            sql += ' AND id = ?'
            params.append(message_id)
        if user_id:
            sql += ' AND user_id = ?'
            params.append(user_id)
        if comment:
            sql += ' AND comment = ?'
            params.append(comment)
        result = cursor.execute(sql, params)
        response = []
        for comment in result.fetchall():
            response.append(
                Comment(
                    id=comment[0],
                    user_id=comment[1],
                    message_id=comment[2],
                    comment=comment[3]
                )
            )

        return response
