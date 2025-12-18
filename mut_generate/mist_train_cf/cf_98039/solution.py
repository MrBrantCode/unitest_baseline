"""
QUESTION:
Write a function `send_email(subject, body, recipients)` that takes three parameters: email subject, email body, and email recipients. Before sending an email, the function should check the user's authentication status by validating their login credentials against an authorized administrator database. Only after successful validation, the function should be allowed to execute. Assume an authorized users database is available.
"""

# Sample authorized users database
authorized_users = {
    "admin1": "password1",
    "admin2": "password2",
    "admin3": "password3"
}

# Function to validate user credentials
def authenticate(username, password):
    if username in authorized_users and authorized_users[username] == password:
        return True
    else:
        return False

def send_email(subject, body, recipients, username, password):
    if authenticate(username, password):
        # Code to send email
        pass
    else:
        raise Exception("Authentication failed. Access denied.")