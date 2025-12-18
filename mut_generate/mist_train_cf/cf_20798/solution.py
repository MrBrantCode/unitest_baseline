"""
QUESTION:
Create a function named `print_message` that takes a string message as input and performs the following operations:

- The message should have a maximum length of 20 characters and contain only alphabetic characters. If not, print "Invalid message!" and exit.
- Print the length of the message.
- Check if the message is a palindrome and print "The message is a palindrome!" if it is.
- Print the message three times, each time in a different color (e.g., red, green, and blue). The function should have a time complexity of O(n), where n is the length of the message.
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