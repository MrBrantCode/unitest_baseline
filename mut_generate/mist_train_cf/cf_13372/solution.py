"""
QUESTION:
Implement a function named `classify_spam_email` that takes in a string representing the content of an email and returns 'spam' or 'not spam' based on the presence of specific spam keywords. The function should be case-insensitive and consider the following keywords as indicative of spam: 'buy', 'discount', 'offer', 'win'.
"""

def classify_spam_email(email_content):
    """
    Classify an email as spam or not spam based on the presence of specific spam keywords.

    Args:
    email_content (str): The content of the email.

    Returns:
    str: 'spam' if the email contains spam keywords, 'not spam' otherwise.
    """
    spam_keywords = ['buy', 'discount', 'offer', 'win']
    email_content = email_content.lower()
    
    for keyword in spam_keywords:
        if keyword in email_content:
            return 'spam'
            
    return 'not spam'