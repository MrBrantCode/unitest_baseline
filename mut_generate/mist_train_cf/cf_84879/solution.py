"""
QUESTION:
Construct a function called `validate_email` that takes three parameters: `user`, `domain`, and `tld`, which represent the username, domain name, and top-level domain respectively. The function should construct an email address using these parameters and then validate its structure. The validation should include checking for the correct use of the '@' symbol, the existence of a valid domain, and a suitable username. The function should return "Email is valid" if the email is valid and "Email is invalid" otherwise. 

The validation should ensure the following conditions:
- The email structure is correct, including the use of the "@" symbol.
- The username only contains alphanumeric characters and underscores.
- The primary domain is alphanumeric, permits hyphens but not as starting or ending characters and includes a top-level domain.
"""

import re

def validate_email(user, domain, tld):
    email = f"{user}@{domain}{tld}"

    # Pattern to ensure the email structure
    emailStructure = re.match('[^@]+@[^@]+\.[^@]+', email)
    
    # Pattern to ensure the username only contains alphanumeric characters and underscores
    usernamePattern = re.match('^\w+$', user)

    # Pattern to ensure the domain is alphanumeric, permits hyphens but not as beginning or ending characters
    domainPattern = re.match('^[a-z0-9]([a-z0-9-]*[a-z0-9])$', domain, re.IGNORECASE)
   
    # Check all conditions
    if emailStructure is None or usernamePattern is None or domainPattern is None:
        return "Email is invalid"
    else:
        return "Email is valid"