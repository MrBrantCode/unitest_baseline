"""
QUESTION:
Classify a given text message as either 'spam' or 'ham'. The function name should be `classify_message`.
"""

def classify_message(message):
    spam_keywords = ["make", "money", "fast", "click", "here", "free", "win", "prize", "discount"]
    message = message.lower()
    for keyword in spam_keywords:
        if keyword in message:
            return 'spam'
    return 'ham'