"""
QUESTION:
Write a function `is_valid_email(email)` to check if a given string is a valid email address. The function should return True if the email address is valid and False otherwise. 

The function must check the following conditions: 
- The email address must contain an "@" symbol.
- The email address must contain a "." symbol.
- The email address must have at least 6 characters.
- The email address must start with a letter.
- The email address must not contain any special characters other than ".", "@", and "_".
- The email address must not have consecutive ".", "@", or "_" symbols.
- The email address must not have a "." immediately after the "@" symbol.
- The email address must have at least one letter before the "@" symbol.
- The email address must have at least two letters after the last "." symbol.
- The email address must not start or end with a ".", "@", or "_" symbol.
- The email address must not have consecutive letters in the domain part (after the last ".") of the email address.

The function must not use any built-in libraries or regular expressions.
"""

def is_valid_email(email):
    # Check condition 1
    if "@" not in email:
        return False
    
    # Check condition 2
    if "." not in email:
        return False
    
    # Check condition 3
    if len(email) < 6:
        return False
    
    # Check condition 4
    if not email[0].isalpha():
        return False
    
    # Check condition 5
    allowed_special_chars = [".", "@", "_"]
    for char in email:
        if not char.isalnum() and char not in allowed_special_chars:
            return False
    
    # Check condition 6
    for i in range(len(email) - 1):
        if email[i] == email[i+1] and email[i] in [".", "@", "_"]:
            return False
    
    # Check condition 7
    if email[email.index("@")+1] == ".":
        return False
    
    # Check condition 8
    if not email[:email.index("@")].isalpha():
        return False
    
    # Check condition 9
    last_dot_index = email.rindex(".")
    if len(email) - last_dot_index < 3:
        return False
    
    # Check condition 10
    if email[0] in [".", "@", "_"] or email[-1] in [".", "@", "_"]:
        return False
    
    # Check condition 11
    domain = email[email.index("@")+1:]
    for i in range(len(domain) - 1):
        if domain[i] == domain[i+1]:
            return False
    
    return True