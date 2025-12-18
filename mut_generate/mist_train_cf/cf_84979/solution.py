"""
QUESTION:
Write a Python function named `is_spam_email` that takes in a string representing the contents of an email and returns a boolean indicating whether the email is spam or not, using a simplified approach such as keyword checking. Assume a predefined list of spam keywords is available.
"""

def is_spam_email(email_contents):
    """
    Checks if an email is spam based on a predefined list of spam keywords.
    
    Args:
    email_contents (str): The contents of the email to be checked.
    
    Returns:
    bool: True if the email is spam, False otherwise.
    """
    
    # Predefined list of spam keywords
    spam_keywords = ["free", "offer", "discount", "buy now"]
    
    # Convert email contents to lowercase to make keyword checking case-insensitive
    email_contents = email_contents.lower()
    
    # Check if any spam keyword is present in the email contents
    for keyword in spam_keywords:
        if keyword in email_contents:
            return True  # Email is spam
    
    return False  # Email is not spam