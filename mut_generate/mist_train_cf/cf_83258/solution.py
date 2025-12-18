"""
QUESTION:
Write a function named `to_leetspeak` that transforms a given alphanumeric string into its corresponding leetspeak representation by replacing the characters 'A' with '4', 'E' with '3', 'I' with '1', 'O' with '0', 'S' with '5', and 'T' with '7'. The function should leave other characters unchanged.
"""

def to_leetspeak(text):
    translation_table = str.maketrans('AEIOSTaeiost', '431057431057')
    return text.translate(translation_table)