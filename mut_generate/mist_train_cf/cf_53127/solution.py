"""
QUESTION:
The function `interpret(command)` should take a string `command` consisting of "G", "()", "(al)", "[o]", and/or "{al}" in some order, and return its interpretation where "G" is interpreted as "G", "()" is interpreted as "o", "(al)" is interpreted as "al", "[o]" is interpreted as "o", and "{al}" is interpreted as "al". The length of `command` is between 1 and 100 inclusive.
"""

def interpret(command):
    return command.replace("()", "o").replace("(al)", "al").replace("[o]", "o").replace("{al}", "al")