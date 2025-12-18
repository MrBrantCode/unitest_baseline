"""
QUESTION:
Create a function named `process_message(message)` that takes a string `message` as input and returns a string as output. The function should check if the `message` exceeds a maximum of 100 characters and return "Error: Message exceeds maximum character limit." if it does. If the `message` does not exceed the limit, the function should process the `message` and return "Message processed successfully."
"""

def process_message(message):
    if len(message) > 100:
        return "Error: Message exceeds maximum character limit."
    else:
        # Process the message here
        return "Message processed successfully."