"""
QUESTION:
Create a function named `count_character_types` that takes a string `s` as input and returns the counts of alphabetic characters, numeric digits, and special characters (non-alphanumeric and non-space characters) in the string. The function should not include spaces as special characters.
"""

def count_character_types(s):
    # Initialize counters
    alphabetic_count = 0
    numeric_count = 0
    special_character_count = 0

    # Iterate through each character in the input string
    for ch in s:
        # Check if character is an alphabet using Python's built-in function
        if ch.isalpha():
            alphabetic_count += 1
            
        # Check if character is a number using Python's built-in function
        elif ch.isdigit():
            numeric_count += 1
            
        # If the character is neither an alphabet nor a number, it's a special character.
        elif ch.isspace() == False:
            special_character_count += 1

    return (alphabetic_count, numeric_count, special_character_count)