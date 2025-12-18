"""
QUESTION:
Implement the `authenticate_user` function, which takes a dictionary of user credentials as input and returns a dictionary containing a "status" field indicating "success" or "fail" based on the authentication result. The function should check if the provided username and password match the valid credentials ("username": "user123", "password": "pass123").
"""

def authenticate_user(credentials: dict) -> dict:
    # Simulate authentication process (dummy example)
    valid_username = "user123"
    valid_password = "pass123"

    if credentials.get("username") == valid_username and credentials.get("password") == valid_password:
        return {"status": "success"}
    else:
        return {"status": "fail"}