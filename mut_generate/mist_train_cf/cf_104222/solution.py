"""
QUESTION:
Construct a function `construct_array` that takes a string as input and returns an array of unique characters from the string. The array should be of the same length as the number of unique characters in the string. Ignore any repeated characters in the string. Implement the function with a time complexity of O(N) and a space complexity of O(N), where N is the length of the input string.
"""

def construct_array(string):
    # Initialize an empty array
    arr = []
    
    # Create a set to store unique characters
    unique_chars = set()
    
    # Iterate over each character in the string
    for char in string:
        # Check if the character is unique and not already present in the set
        if char not in unique_chars:
            # Add the character to the set and the array
            unique_chars.add(char)
            arr.append(char)
    
    return arr