"""
QUESTION:
You received a whatsup message from an unknown number. Could it be from that girl/boy with a foreign accent you met yesterday evening?

Write a simple regex to check if the string contains the word hallo in different languages.

These are the languages of the possible people you met the night before:

* hello - english
* ciao - italian
* salut - french
* hallo - german
* hola - spanish
* ahoj - czech republic
* czesc - polish

By the way, how cool is the czech republic hallo!!


PS. you can assume the input is a string.
PPS. to keep this a beginner exercise you don't need to check if the greeting is a subset of word ('Hallowen' can pass the test)

PS. regex should be case insensitive to pass the tests
"""

def contains_greeting(message: str) -> bool:
    """
    Checks if the given message contains any of the greetings in different languages.

    Parameters:
    - message (str): The message to be checked.

    Returns:
    - bool: True if the message contains any of the greetings, False otherwise.
    """
    greetings = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    return any(greeting in message.lower() for greeting in greetings)