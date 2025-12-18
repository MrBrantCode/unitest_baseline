"""
QUESTION:
Develop a function named `is_spam_email` that takes an email text as input and returns a boolean indicating whether the email is spam or not. The function should use a predefined list of spam keywords and phrases to identify spam emails. The function should be case-insensitive and also check for suspicious links or attachments. The spam detection should be based on a threshold that can be adjusted.
"""

def is_spam_email(email_text, threshold=3):
    """
    This function checks if an email is spam or not based on a list of spam keywords and phrases.

    Args:
        email_text (str): The text of the email.
        threshold (int, optional): The minimum number of spam indicators required to classify an email as spam. Defaults to 3.

    Returns:
        bool: True if the email is spam, False otherwise.
    """

    # Define spam keywords
    spam_keywords = ['congratulations', 'won', 'free', 'trip', 'click here', 'more info']

    # Define spam phrases
    spam_phrases = ['claim your prize', 'limited time offer', 'click to download']

    # Initialize spam count
    spam_count = 0

    # Tokenize the email text into sentences or phrases
    sentences = email_text.lower().split('. ')

    # Check each sentence or phrase for spam keywords and phrases
    for sentence in sentences:
        for keyword in spam_keywords:
            if keyword in sentence:
                spam_count += 1
        for phrase in spam_phrases:
            if phrase in sentence:
                spam_count += 1

    # Check for suspicious links or attachments
    if 'http://' in email_text.lower() or 'https://' in email_text.lower():
        spam_count += 1
    if 'click to download' in email_text.lower() or 'download attachment' in email_text.lower():
        spam_count += 1

    # Return True if spam count is above the threshold, False otherwise
    return spam_count >= threshold