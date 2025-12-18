"""
QUESTION:
Create a function named `greet_user` that takes user input from the console and outputs a greeting message. If the input is 'John', 'Jane', or 'James', output a specific greeting for each of those names. Otherwise, output 'Hello [name]'.
"""

def greet_user(name):
    if name == 'John':
        return "Greetings, oh wise one!"
    elif name == 'Jane':
        return "Greetings, oh mighty one!"
    elif name == 'James':
        return "Greetings, oh great one!"
    else:
        return "Hello " + name