from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'john', 'asdf')
]

username_mapping = {u.username: u for u in users}
user_id_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return user_id_mapping.get(user_id, None)