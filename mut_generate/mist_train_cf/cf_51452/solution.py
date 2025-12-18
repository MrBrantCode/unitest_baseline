"""
QUESTION:
Create a function named `compare_phrase_sets` that takes two input strings `phrase1` and `phrase2`, each containing words and spaces, and returns `True` if they have identical unique word phrases, considering word repetition, and `False` otherwise. The function should also validate the input string formats to ensure they are in correct lexical syntax, containing only words and spaces. If the input strings are not valid, the function should return an error message.
"""

def compare_phrase_sets(phrase1, phrase2):
    # Validate input string formats
    if not isinstance(phrase1, str) or not isinstance(phrase2, str):
        return "Error: Inputs should be strings"
        
    # Check if they are in correct lexical syntax
    if not phrase1.replace(" ", "").isalpha() or not phrase2.replace(" ", "").isalpha():
        return "Error: The input strings should only contain words and spaces"
        
    # Sort the words within each phrase and compare
    sorted_entities_phrase1 = sorted(phrase1.split())
    sorted_entities_phrase2 = sorted(phrase2.split())

    return sorted_entities_phrase1 == sorted_entities_phrase2