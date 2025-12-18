"""
QUESTION:
Implement the `validate_social_network_user` function that takes in two parameters: `details` (a dictionary containing user details, including the email address) and `logged_in_user` (the username of the currently logged-in user, if any). The function should perform the following checks: 
- If the user's email is not provided in the `details` dictionary, return an error message indicating the requirement for the email address.
- If the `logged_in_user` is not empty and the email address associated with the social network (`details['email']`) does not match the email address of the logged-in user (`logged_in_user`), return an error message indicating the mismatch. 
The function should return an error message if any of the validation checks fail, or it should return `None` if the user information is valid.
"""

def validate_social_network_user(details, logged_in_user):
    if not details.get('email'):
        error = "Sorry, but your social network (Facebook or Google) needs to provide us your email address."
        return error

    if logged_in_user:
        if logged_in_user.lower() != details.get('email').lower():
            error = "Sorry, but you are already logged in with another account, and the email addresses do not match. Try logging out first, please."
            return error

    return None