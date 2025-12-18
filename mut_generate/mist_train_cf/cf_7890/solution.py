"""
QUESTION:
Create a function named `get_nicknames` that takes a list of Lord of the Rings characters as input and returns a list of their corresponding nicknames. The function should have a time complexity of O(n), where n is the number of characters in the input list, and return the nicknames in alphabetical order. The output list should contain unique nicknames only, and any special characters in the nicknames should be converted to their corresponding ASCII codes. Each nickname's first letter should be capitalized, and the rest of the letters should be in lowercase.
"""

def get_nicknames(characters):
    nicknames = set()
    
    for character in characters:
        # Convert character's nickname to lowercase
        nickname = character.lower()
        
        # Capitalize the first letter
        nickname = nickname.capitalize()
        
        # Replace special characters with ASCII codes
        nickname = ''.join(str(ord(char)) if not char.isalnum() else char for char in nickname)
        
        # Add the nickname to the set
        nicknames.add(nickname)
    
    # Sort the nicknames alphabetically and convert back to a list
    return sorted(nicknames)