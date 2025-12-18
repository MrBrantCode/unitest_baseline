"""
QUESTION:
Complete the message creation logic by implementing the `create_message` function. The function should take a list of destroyed instances as input and return a message based on the instances. The message creation logic should be implemented considering the following conditions:

*   If the node associated with a destroyed instance is already destroyed, it should not be added to the message.
*   If the node associated with a destroyed instance is fake, it should not be added to the message immediately.
"""

def create_message(destroyed_instances):
    message = []
    for instance in destroyed_instances:
        message.append(f"Instance {instance} destroyed")
    return message