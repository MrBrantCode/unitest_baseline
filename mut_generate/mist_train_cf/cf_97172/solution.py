"""
QUESTION:
Generate a function called `generate_unique_id` that takes a string input and returns a unique integer ID. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

def generate_unique_id(input_string):
    # Initialize the unique ID to 0
    unique_id = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        # Calculate the ASCII value of the character
        ascii_value = ord(char)
        
        # Update the unique ID by adding the ASCII value
        unique_id += ascii_value
    
    return unique_id