import json

# Default credentials
default_username = 'root'
default_password = 'root'

def save_credentials(username, password):
    credentials = {
        'username': username,
        'password': password
    }
    with open('credentials.json', 'w') as file:
        json.dump(credentials, file)

def load_credentials():
    try:
        with open('credentials.json', 'r') as file:
            credentials = json.load(file)
            return credentials['username'], credentials['password']
    except (FileNotFoundError, json.JSONDecodeError):
        return default_username, default_password
