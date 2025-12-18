"""
QUESTION:
Create a function `modify_string` that takes a string as input and returns a tuple. The function should perform the following operations on the string: remove all non-alphabetical characters, convert all uppercase letters to lowercase, reverse the order of the characters, and count the number of vowels in the modified string. The function should return the modified string and the vowel count as a tuple.
"""

def modify_string(string):
    # Remove non-alphabetical characters
    modified_string = ''.join(c for c in string if c.isalpha())

    # Convert uppercase letters to lowercase
    modified_string = modified_string.lower()

    # Reverse the order of characters
    modified_string = modified_string[::-1]

    # Count the number of vowels
    vowel_count = sum(1 for c in modified_string if c in 'aeiou')

    # Return the modified string and vowel count as a tuple
    return modified_string, vowel_count