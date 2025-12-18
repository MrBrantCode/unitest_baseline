"""
QUESTION:
Write a function `find_first_non_duplicate` that takes a string as input and returns the first non-duplicate character. The function should handle cases where the string contains uppercase and lowercase letters, special characters, and numbers. The function should have a time complexity of O(n) and not use any additional libraries. The input string can have a maximum length of 10^6.
"""

def find_first_non_duplicate(string):
    # Create a dictionary to store the count of each character
    character_count = {}
    
    # Convert the string to lowercase
    string = string.lower()
    
    # Iterate over each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        # Otherwise, add the character to the dictionary with a count of 1
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    
    # Iterate over the original string to find the first non-duplicate character
    for char in string:
        # If the count of the character is 1, return it
        if character_count[char] == 1:
            return char
    
    # If no non-duplicate character is found, return None
    return None