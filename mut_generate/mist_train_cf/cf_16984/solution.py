"""
QUESTION:
Create a function called `contains_all_alphabets` that checks if a given string contains all alphabets (both lowercase and uppercase) at least once. The function must have a time complexity of O(n), where n is the length of the string. It should not use any built-in functions or libraries that directly check for alphabet characters, regular expressions, or external libraries. It should be case-insensitive and handle both ASCII and Unicode strings efficiently. The function should return False immediately if the string does not contain at least one occurrence of each alphabet.
"""

def contains_all_alphabets(phrase):
    # Create a set to keep track of unique alphabets
    alphabets = set()

    # Iterate over each character in the string
    for char in phrase:
        # Check if the character is a lowercase alphabet
        if ord('a') <= ord(char.lower()) <= ord('z'):
            alphabets.add(char.lower())

        # Break the loop if all alphabets have been found
        if len(alphabets) == 26:
            return True

    # Return False if all alphabets were not found
    return False