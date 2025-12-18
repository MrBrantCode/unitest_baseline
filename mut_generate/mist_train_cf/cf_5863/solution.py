"""
QUESTION:
Write a function `extract_full_name` that takes a string as input, extracts the full name consisting of a first name and a last name separated by a single space, and returns the extracted full name. The input string may start with a greeting ("Hello!", "Hi!", or "Hey!") followed by a space, and may contain additional text after the last name. If the input string does not start with a valid greeting, return "Error: Invalid greeting".
"""

def extract_full_name(input_string):
    greetings = ["Hello!", "Hi!", "Hey!"]
    full_name = ""
    
    # Check if input string starts with a valid greeting
    if input_string.startswith(tuple(greetings)):
        # Find the index of the space after the greeting
        space_index = input_string.index(" ") + 1
        
        # Find the index of the second space, which separates the first and last names
        second_space_index = input_string.find(" ", space_index)
        
        # Extract the full name based on the indices
        if second_space_index != -1:
            full_name = input_string[space_index:second_space_index]
        else:
            full_name = input_string[space_index:]
    else:
        # Return an error message if no valid greeting is found
        full_name = "Error: Invalid greeting"
    
    return full_name