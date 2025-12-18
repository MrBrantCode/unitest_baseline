"""
QUESTION:
Write a function called `count_characters` that takes a string as input, excludes special characters (non-alphanumeric), and returns a dictionary where the keys are the alphanumeric characters from the string and the values are their corresponding counts. The function should achieve a time complexity of O(n), where n is the length of the string, and a space complexity of O(1) relative to the input size, assuming the size of the character set is constant.
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