"""
QUESTION:
Create a function `generate_unique_username(name, existing_usernames, max_length)` that generates a unique username based on a given name. The function should take into account the maximum length of the username and ensure that the generated username is unique within a given list of existing usernames. The function should return a unique username based on the given name, ensuring that it does not exceed the maximum length and is unique within the existing usernames list. If it's not possible to generate a unique username within the maximum length, the function should return None.
"""

def generate_unique_username(name, existing_usernames, max_length):
    base_username = name.lower().replace(" ", "_")
    
    if base_username not in existing_usernames and len(base_username) <= max_length:
        return base_username
    
    for i in range(2, 1000):  
        unique_username = f"{base_username}{i}"
        if len(unique_username) <= max_length and unique_username not in existing_usernames:
            return unique_username
    
    return None