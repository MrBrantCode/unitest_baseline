"""
QUESTION:
Create a function `greet_user` that takes a `name` parameter and returns a string containing the following information: a greeting with the user's name, the number of characters in the name, and the reversed name in uppercase. The function should be a Django view and the output string should be rendered in a template.
"""

def greet_user(name):
    # Calculate the number of characters in the name
    num_characters = len(name)

    # Reverse the name and convert it to uppercase
    reversed_name = name[::-1].upper()

    # Build the output string
    output_string = f"Hello {name}! Your name has {num_characters} characters. Additionally, the reverse of your name is {reversed_name}."
    return output_string