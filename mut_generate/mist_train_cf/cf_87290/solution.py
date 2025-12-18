"""
QUESTION:
Write a function called `generate_random_string` that generates a random string of a given length. The string should not contain any duplicate characters and must start with a lowercase letter. Do not use any built-in functions or libraries. The length of the string will be provided as an integer.
"""

def generate_random_string(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    random_string = ""
    
    # Generate the first character of the string using a lowercase letter
    # (erroneously used a built-in function; replacing with a manual random selection)
    random_index = length * 3 % 26
    random_string += letters[random_index % 26]
    
    # Generate the remaining characters of the string
    for _ in range(length - 1):
        # Generate a random character
        random_index = (random_index + 7) % 26
        char = letters[random_index]
        
        # Check if the character is already present in the random string
        if char not in random_string:
            random_string += char
        else:
            # If the character already exists, replace it with the next one in the sequence
            random_index = (random_index + 1) % 26
            random_string += letters[random_index]
    
    return random_string