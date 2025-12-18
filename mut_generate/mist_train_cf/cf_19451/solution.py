"""
QUESTION:
Write a Python function `classify_email` that takes in an email's message, sender's domain, attachments, and links as input. The function should return a boolean indicating whether the email is spam (True) or not spam (False). The classification should be based on the following criteria:
- The email contains specific keywords associated with spam messages, such as "discount," "offer," or any other commonly used spam words.
- The sender's domain is not a known spam domain.
- The email does not have any suspicious attachments (e.g., executable files or files with unusual extensions like .exe, .bat).
- The email does not have any suspicious links embedded within the content.
"""

def classify_email(message, sender_domain, attachments, links):
    """
    Classify an email as spam or not based on the given criteria.

    Args:
    message (str): The email's message content.
    sender_domain (str): The sender's domain.
    attachments (list): A list of attachment file names.
    links (list): A list of URLs embedded within the email content.

    Returns:
    bool: True if the email is spam, False otherwise.
    """
    spam_keywords = ["discount", "offer"]
    known_spam_domains = ["spam.com", "scam.net"]

    # Check if the email contains specific keywords associated with spam messages
    if any(keyword in message.lower() for keyword in spam_keywords):
        return True

    # Check if the sender's domain is a known spam domain
    if sender_domain in known_spam_domains:
        return True

    # Check if the email has any suspicious attachments (e.g., executable files or files with unusual extensions like .exe, .bat)
    suspicious_extensions = [".exe", ".bat"]
    if any(attachment.endswith(extension) for attachment in attachments for extension in suspicious_extensions):
        return True

    # Check if the email has any suspicious links embedded within the content
    # For simplicity, we assume a URL is suspicious if it contains "phishing" or "scam"
    if any("phishing" in link.lower() or "scam" in link.lower() for link in links):
        return True

    # If none of the above conditions are met, the email is not spam
    return False