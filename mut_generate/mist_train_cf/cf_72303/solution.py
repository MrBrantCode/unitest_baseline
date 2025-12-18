"""
QUESTION:
Create a function `say_hello` that takes a list of names as input and prints individual greetings for each name. The function should handle potential edge cases by checking if the input is a list and not empty. It should also handle non-string elements in the list, catching any exceptions that may occur during the greeting process. If an error occurs with an element, the function should print an error message and continue processing the next element in the list.
"""

def say_hello(name_list):
    if not isinstance(name_list, list):
        print("Error: Input is not a list!")
        return
    if len(name_list) == 0:
        print("Error: List is empty!")
        return
    for name in name_list:
        try:
            print("Greetings " + name + "!")
        except TypeError:
            print("Error: Non-string value detected in the list")