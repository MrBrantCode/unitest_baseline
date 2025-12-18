"""
QUESTION:
Create a function `classify_email` that takes in a string `email_content` and returns a classification of the email as 'spam', 'phishing', or 'not spam'. The function should use predefined sets of spam and phishing words to classify the email. The email is considered spam if it contains more than 5 spam words and phishing if it contains more than 3 phishing words. The function should be case-insensitive and should split the email content into individual words using spaces and punctuation.
"""

import re
from typing import Set

def classify_email(email_content: str, spam_words: Set[str], phishing_words: Set[str]) -> str:
    """
    Classify an email as 'spam', 'phishing', or 'not spam' based on its content.

    Args:
    email_content (str): The content of the email.
    spam_words (Set[str]): A set of words commonly found in spam emails.
    phishing_words (Set[str]): A set of words commonly found in phishing emails.

    Returns:
    str: The classification of the email ('spam', 'phishing', or 'not spam').
    """

    # Split the email content into individual words, ignoring case and punctuation
    words = re.findall(r'\b\w+\b', email_content.lower())

    # Initialize counters for spam and phishing words
    spam_count = sum(1 for word in words if word in spam_words)
    phishing_count = sum(1 for word in words if word in phishing_words)

    # Classify the email based on the counts
    if spam_count > 5:
        return 'spam'
    elif phishing_count > 3:
        return 'phishing'
    else:
        return 'not spam'