"""
QUESTION:
Create a function `email_spam_classifier` that takes an email text as input and returns a boolean indicating whether the email is spam or not. The function should be based on a naive Bayes classifier and should handle text preprocessing, feature extraction, and model training. The dataset for training the model should consist of labeled spam and non-spam emails.
"""

import re
from collections import defaultdict
from math import log

def email_spam_classifier(email_text, spam_emails, non_spam_emails):
    """
    Classify an email as spam or not using a naive Bayes classifier.

    Parameters:
    email_text (str): The text of the email to classify.
    spam_emails (list): A list of spam emails for training.
    non_spam_emails (list): A list of non-spam emails for training.

    Returns:
    bool: True if the email is classified as spam, False otherwise.
    """

    # Pre-processing
    def clean_text(text):
        text = text.lower()
        text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
        text = re.sub(r'\W', ' ', text)  # Remove non-word characters
        text = re.sub(r'\s+', ' ', text)  # Remove multiple spaces
        return text

    email_text = clean_text(email_text)

    # Feature Extraction
    def extract_features(emails):
        features = defaultdict(int)
        for email in emails:
            email = clean_text(email)
            words = email.split()
            for word in words:
                features[word] += 1
        return features

    spam_features = extract_features(spam_emails)
    non_spam_features = extract_features(non_spam_emails)

    # Naive Bayes Classifier
    def classify(email, spam_features, non_spam_features):
        spam_prob = log(len(spam_emails) / (len(spam_emails) + len(non_spam_emails)))
        non_spam_prob = log(len(non_spam_emails) / (len(spam_emails) + len(non_spam_emails)))
        for word in email.split():
            spam_prob += log((spam_features[word] + 1) / (len(spam_features) + len(non_spam_features)))
            non_spam_prob += log((non_spam_features[word] + 1) / (len(non_spam_features) + len(spam_features)))
        return spam_prob > non_spam_prob

    return classify(email_text, spam_features, non_spam_features)