"""
QUESTION:
Create a function called `modify_string` that takes a string as input. The function should remove all non-alphabetical characters from the string, convert all uppercase letters to lowercase, reverse the order of the characters, and count the number of vowels in the modified string. The function should return a tuple containing the modified string and the vowel count.
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