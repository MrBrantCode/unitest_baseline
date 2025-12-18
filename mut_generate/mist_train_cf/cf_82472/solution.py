"""
QUESTION:
Create a function named `check_email` that takes a string as input, checks if it's a valid email, identifies the domain of the email, and counts the number of characters before and after the '@' symbol. The function should return a dictionary containing the validity of the email, the count of the characters in the user part, the name of the domain, and the count of the characters in the domain name if the email is valid. If the email is invalid, the function should return False. A valid email should have a non-empty username, a non-empty domain name, and a non-empty domain extension. The function should handle cases where the email string does not contain '@' or '.' or does not follow the correct order of these characters.
"""

def check_email(email):
    try:
        user, domain = email.split('@')
        domain_name, domain_extension = domain.split('.')
        
        if len(user) < 1 or len(domain_name) < 1 or len(domain_extension) < 1:
            return False
        else:
            return {'validity': True, 
                    'user_character_count': len(user),
                    'domain': domain_name,
                    'domain_character_count': len(domain_name)}
    except ValueError:
        return False