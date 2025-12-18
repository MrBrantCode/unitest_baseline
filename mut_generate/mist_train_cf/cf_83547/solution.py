"""
QUESTION:
Create a function called `remove_spam` that takes a string `text` and a list of spam words `spam_words` as input. The function should return the input text with all occurrences of spam words removed, excluding false positives that appear in a list of legitimate phrases `legitimate_phrases`.
"""

def remove_spam(text, spam_words, legitimate_phrases):
    """
    Removes spam words from the given text excluding false positives in legitimate phrases.

    Args:
        text (str): The input text to be cleaned.
        spam_words (list): A list of spam words to be removed.
        legitimate_phrases (list): A list of legitimate phrases to avoid false positives.

    Returns:
        str: The cleaned text with spam words removed.
    """
    words = text.split()
    cleaned_text = []

    for word in words:
        if word.lower() not in [spam_word.lower() for spam_word in spam_words if spam_word.lower() not in [phrase.lower() for phrase in legitimate_phrases]]:
            cleaned_text.append(word)

    return ' '.join(cleaned_text)