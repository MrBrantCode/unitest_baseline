"""
QUESTION:
Create a function named `semantic_decoder` that takes a single character as input and returns its corresponding semantic value based on its position in the English alphabet (with 'a' as 1, 'b' as 2, and so on). The function should be case-insensitive and return `None` if the input character is not a letter.
"""

def semantic_decoder(character):
    # Define alphabet in lowercase. You can define your own alphabet system here.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Check if the character exists in the alphabet
    if character.lower() not in alphabet:
        return None

    # Get the index of the character in alphabet (add 1 due to 0 based indexing)
    sem_value = alphabet.index(character.lower()) + 1

    return sem_value