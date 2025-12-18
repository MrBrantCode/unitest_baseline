"""
QUESTION:
Implement the `validatePassword` function to validate a password based on the following criteria:

- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character from the set {!, @, #, $, %, ^, &, *}.

The function should take a string `password` as input and return a boolean value indicating whether the password meets the specified criteria.

Function Signature:
```python
def validatePassword(password: str) -> bool
```
"""

import re

def validatePassword(password: str) -> bool:
    # Check if the password length is at least 8 characters
    if len(password) < 8:
        return False
    
    # Check if the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password) or not re.search(r"\d", password) or not re.search(r"[!@#$%^&*]", password):
        return False
    
    return True