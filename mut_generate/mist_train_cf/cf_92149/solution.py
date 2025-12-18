"""
QUESTION:
Create a function called `process_message` that takes a string `message` as input and returns a string as output. The function should check if the length of `message` is within the limit of 100 characters. If the length exceeds the limit, the function should return an error message "Error: Message exceeds maximum character limit." Otherwise, the function should process the message and return a success message "Message processed successfully."
"""

def process_message(message):
    if len(message) > 100:
        return "Error: Message exceeds maximum character limit."
    else:
        # Process the message here
        return "Message processed successfully."