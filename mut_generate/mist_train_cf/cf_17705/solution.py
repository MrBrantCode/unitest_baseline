"""
QUESTION:
Create a class named 'Greeting' with a method 'find_greeting' that takes a name and returns a greeting message. The method should return specific messages for 'Alice' and 'Bob', and a generic message for any other name.
"""

def find_greeting(name):
    """
    Returns a personalized greeting message based on the given name.

    Args:
        name (str): The name to generate a greeting for.

    Returns:
        str: A greeting message.
    """
    if name == "Alice":
        return "Hi Alice!"
    elif name == "Bob":
        return "Hi Bob!"
    else:
        return "Hello!"