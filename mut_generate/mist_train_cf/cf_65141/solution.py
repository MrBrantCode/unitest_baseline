"""
QUESTION:
Design a login system with the following functions: `register(username, password)` and `login(username, password)`. The system should have the following requirements and restrictions:

- The `register(username, password)` function should create a new user account if the username does not already exist. 
- The password must contain at least one lowercase letter, one uppercase letter, one number, and one special character.
- The `login(username, password)` function should allow a user to log in if the username and password match. 
- If the username and password do not match, the system should increment the number of failed login attempts for that user. 
- If a user has more than 2 failed login attempts, their account should be locked, and they should not be able to log in until they reset their password or until the lock is lifted.
"""

import re

users = {}

def login_system(username, password, action):
    if action == "register":
        return register(username, password)
    elif action == "login":
        return login(username, password)

def register(username, password):
    if username in users:
        print("Username already exists")
        return False

    if not re.search("[a-z]", password):
        print("Password must contain at least one lowercase letter")
        return False

    if not re.search("[A-Z]", password):
        print("Password must contain at least one uppercase letter")
        return False

    if not re.search("[0-9]", password):
        print("Password must contain at least one number")
        return False

    if not re.search("[_!@#$%^&*()<>?/\|}{~:]", password):
        print("Password must contain at least one special character")
        return False

    users[username] = {"password": password, "attempts": 0 }
    print("User created successfully")
    return True

def login(username, password):
    if username not in users:
        print("Username does not exist")
        return False

    if users[username]["attempts"] > 2:
        print("Account is locked due to too many unsuccessful login attempts")
        return False

    if users[username]["password"] != password:
        users[username]["attempts"] += 1
        return False

    users[username]["attempts"] = 0
    print("Login successful")
    return True