"""
QUESTION:
Write a function `extract_words` that takes a list of strings and a single character as inputs. The function should return a list of words that start with the given character (case-insensitive) but do not contain the character in any other position. The output list should be sorted alphabetically.
"""

def extract_words(strings, letter):
    """
    Extract words that start with the given character (case-insensitive) 
    but do not contain the character in any other position.

    Args:
    strings (list): A list of strings.
    letter (str): A single character.

    Returns:
    list: A list of words that meet the condition, sorted alphabetically.
    """
    extracted_words = []
    letter = letter.lower()
    for string in strings:
        words = string.split()
        for word in words:
            if word.lower().startswith(letter) and letter not in word.lower()[1:]:
                extracted_words.append(word)
    extracted_words.sort()
    return extracted_words