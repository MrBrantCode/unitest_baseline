"""
QUESTION:
Create a function called `extract_full_name` that takes a string as input and extracts the full name from it. The full name should consist of a first name and a last name, separated by a single space. The input string will start with a greeting ("Hello!", "Hi!", or "Hey!") followed by a space. The function should handle cases where the input string does not start with a valid greeting and return an error message. The function should also handle cases where the input string contains multiple spaces between the first name and last name.
"""

def extract_full_name(input_string):
    greetings = ["Hello!", "Hi!", "Hey!"]
    full_name = ""
    
    # Check if input string starts with a valid greeting
    if input_string.startswith(tuple(greetings)):
        # Split the input string into parts
        parts = input_string.split(" ")
        
        # Remove the greeting and the phrase "My name is"
        parts = parts[2:]
        
        # Extract the full name
        full_name = " ".join(parts)
    else:
        # Return an error message if no valid greeting is found
        full_name = "Error: Invalid greeting"
    
    return full_name