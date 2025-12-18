"""
QUESTION:
Implement the function `login(username, password)` that takes a username and a password as input and checks if the entered password is correct. The function should return a generic error message if the password is incorrect, without specifying whether the username or the password was incorrect. Do not provide any additional information about the validity of the username or password in the error message.
"""

def login(username, password):
    if password == "correct_password":
        return "Login successful!"
    else:
        return "Incorrect username or password, please try again."