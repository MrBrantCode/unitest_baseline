"""
QUESTION:
Replace vowels in a given text with a specified character, excluding the vowel 'y', while keeping track of the total number of replaced vowels and the number of vowels replaced at a specific position. Implement a function `replace_vowels` that takes three parameters: `text`, `char`, and `position`. The function should return the updated text, the total count of replaced vowels, and the count of vowels replaced at the specified position. The function should iterate through each character in the given text and replace the vowels according to the specified rules.
"""

def replace_vowels(text, char, position):
    """
    Replaces vowels in a given text with a specified character, 
    excluding the vowel 'y', while keeping track of the total number 
    of replaced vowels and the number of vowels replaced at a specific position.

    Args:
    text (str): The input text.
    char (str): The character to replace vowels with.
    position (int): The position to count vowel replacements.

    Returns:
    tuple: A tuple containing the updated text, the total count of replaced vowels, 
    and the count of vowels replaced at the specified position.
    """

    count = 0
    positionCount = 0
    updated_text = ""

    for i, ch in enumerate(text):
        if ch.lower() in 'aeiou':
            count += 1
            if i == position - 1:  # Adjust position to 0-indexed
                positionCount += 1
            updated_text += char
        else:
            updated_text += ch

    return updated_text, count, positionCount