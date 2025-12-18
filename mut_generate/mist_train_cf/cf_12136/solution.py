"""
QUESTION:
Create a function `classify_spam_email(email_message, sender_domain, spam_domains, spam_keywords)` that takes in the email message, sender's domain, a list of known spam domains, and a list of spam keywords. Return 'Spam' if the email contains any of the spam keywords and the sender's domain is not in the known spam domains list, otherwise return 'Not Spam'.
"""

def classify_spam_email(email_message, sender_domain, spam_domains, spam_keywords):
    """
    Classify an email as spam or not spam based on the presence of spam keywords and the sender's domain.

    Args:
        email_message (str): The content of the email.
        sender_domain (str): The domain of the sender's email.
        spam_domains (list): A list of known spam domains.
        spam_keywords (list): A list of spam keywords.

    Returns:
        str: 'Spam' if the email is classified as spam, 'Not Spam' otherwise.
    """

    # Check if the sender's domain is in the list of known spam domains
    is_known_spam_domain = sender_domain in spam_domains

    # Check if any of the spam keywords are present in the email message
    contains_spam_keyword = any(keyword in email_message for keyword in spam_keywords)

    # If the email contains a spam keyword and the sender's domain is not a known spam domain, classify as spam
    if contains_spam_keyword and not is_known_spam_domain:
        return 'Spam'
    else:
        return 'Not Spam'