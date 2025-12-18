"""
QUESTION:
Write a function named `count_characters` that takes a string as input and returns a dictionary where the keys are alphanumeric characters (letters and digits) in the string and the values are their respective counts. The function should have a time complexity of O(n), where n is the length of the string. Exclude non-alphanumeric characters from the dictionary.
"""

def count_characters(string):
    # Initialize an empty dictionary
    character_counts = {}
    
    # Iterate through each character in the string
    for char in string:
        # Check if the character is a letter or a digit
        if char.isalnum():
            # If the character is already in the dictionary, increment its count
            if char in character_counts:
                character_counts[char] += 1
            # If the character is not in the dictionary, add it with a count of 1
            else:
                character_counts[char] = 1
    
    # Return the resulting dictionary
    return character_counts