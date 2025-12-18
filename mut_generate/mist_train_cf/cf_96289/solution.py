"""
QUESTION:
Create a function called `print_message` that takes a string message as input. The message should contain only alphabetic characters and have a maximum length of 20 characters. The function should print the length of the message, check if it's a palindrome and print a message if so, and then print the message three times in different colors. The function should have a time complexity of O(n), where n is the length of the message.
"""

def print_message(message):
    if len(message) > 20 or not message.isalpha():
        print("Invalid message!")
        return

    print(f"Length of message: {len(message)}")

    if message == message[::-1]:
        print("The message is a palindrome!")

    colors = ['red', 'green', 'blue']
    for i in range(3):
        print(f"\033[1;{30 + i};40m{message}\033[0m")