"""
ORIGINAL QUESTION:
Create a function named `print_message` that takes a string `message` as input. The function should first check if `message` contains only alphabetic characters and its length does not exceed 20 characters. If the message is valid, the function should print the length of the message, followed by printing the message three times in different colors (red, green, and blue). If the message is invalid, the function should print an error message and return.
"""

def print_message(message):
    # Check if message contains only alphabetic characters
    if not message.isalpha():
        print("Message can only contain alphabetic characters.")
        return
    
    # Check if message length exceeds 20 characters
    if len(message) > 20:
        print("Message length cannot exceed 20 characters.")
        return
    
    # Print the length of the message
    print("Message length:", len(message))
    
    # Print the repeated message in different colors
    colors = ['red', 'green', 'blue']
    for i in range(3):
        print("\033[1m\033[3{}m{}\033[0m".format(i+1, message))