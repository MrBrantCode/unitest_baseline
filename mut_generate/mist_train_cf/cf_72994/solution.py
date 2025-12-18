"""
QUESTION:
Write a recursive function named `print_message` that prints "Goodbye Universe" exactly 40 times without using loops or global/static variables. Ensure the function does not cause a stack overflow. The function should be able to accept an optional integer argument to specify the number of times the message is printed; if no argument is provided, it should default to 40.
"""

def print_message(times=40):
    if times == 0:
        return
    else:
        print("Goodbye Universe")
        print_message(times - 1)