"""
QUESTION:
Write a function `categorize_words` that takes a string of text as input and categorizes each word in the text based on the following rules:
- If a word starts with a vowel (a, e, i, o, u), it belongs to the "Vowel" category.
- If a word starts with a consonant and ends with a vowel, it belongs to the "Consonant-Vowel" category.
- If a word starts with a consonant and ends with a consonant, it belongs to the "Consonant-Consonant" category.
- If a word consists of only digits, it belongs to the "Numeric" category.
- If a word consists of a combination of letters and digits, it belongs to the "Alphanumeric" category.
- If a word contains any special characters (such as !, ?, #, etc.), it belongs to the "Special Characters" category.
The function should return the categorization of each word in the text.
"""

def categorize_words(text):
    """
    Categorize each word in the text based on the given rules.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary where keys are words and values are their respective categories.
    """
    vowels = 'aeiou'
    words = text.split()
    categories = {}

    for word in words:
        if word[0].lower() in vowels:
            categories[word] = 'Vowel'
        elif word[-1].lower() in vowels:
            categories[word] = 'Consonant-Vowel'
        elif word.isalpha():
            categories[word] = 'Consonant-Consonant'
        elif word.isdigit():
            categories[word] = 'Numeric'
        elif word.isalnum():
            categories[word] = 'Alphanumeric'
        else:
            categories[word] = 'Special Characters'

    return categories