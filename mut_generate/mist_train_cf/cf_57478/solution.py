"""
QUESTION:
Write a function `process_phrase` that takes a string `phrase` as input, converts it to lower case, separates vowels and consonants, counts the number of vowels and consonants, and replaces all vowels with '$' symbol. The function should return the lower case phrase, the count of vowels, the count of consonants, and the phrase with vowels replaced. The function should consider only alphabetic characters and ignore other characters.
"""

def process_phrase(phrase):
    """
    This function takes a string phrase as input, converts it to lower case, 
    separates vowels and consonants, counts the number of vowels and consonants, 
    and replaces all vowels with '$' symbol.

    Args:
        phrase (str): The input phrase to be processed.

    Returns:
        tuple: A tuple containing the lower case phrase, the count of vowels, 
        the count of consonants, and the phrase with vowels replaced.
    """

    # Convert to lower case letter
    phrase_lower = phrase.lower()

    # Initialize counters and lists
    vowels_count = 0
    consonants_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Separation of vowels and consonants
    for char in phrase_lower:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    # Replace vowels with '$' symbol
    new_phrase = ''.join(['$' if char in vowels else char for char in phrase_lower])

    return phrase_lower, vowels_count, consonants_count, new_phrase