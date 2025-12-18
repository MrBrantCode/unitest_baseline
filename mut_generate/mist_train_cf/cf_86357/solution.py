"""
QUESTION:
Write a function `count_occurrences` that takes a string of maximum 1000 characters and a single character as input. The function should return the number of occurrences of the given character in the string, considering both uppercase and lowercase characters as separate entities. The input character must be an alphabet; if not, the function should return an error message.
"""

def count_occurrences(string, character):
    # Check if character is an alphabet
    if not character.isalpha():
        return "Error: Character must be an alphabet."

    # Initialize counter
    count = 0

    # Iterate over each character in the string
    for char in string:
        # Check if the character matches the given character (case-sensitive)
        if char == character:
            count += 1
        # Check if the lowercase character matches the given character
        elif char.lower() == character.lower():
            count += 1

    return count