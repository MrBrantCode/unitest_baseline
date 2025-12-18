"""
QUESTION:
Write a function `count_occurrences(string, character)` that takes a string of maximum 1000 characters and a single alphabet character as input. The function should return the number of occurrences of the character in the string, considering both uppercase and lowercase characters as separate entities. If the input character is not an alphabet, return an error message.
"""

def count_occurrences(string, character):
    if not character.isalpha():
        return "Error: Character must be an alphabet."

    count = 0
    for char in string:
        if char == character or char.lower() == character.lower():
            count += 1

    return count