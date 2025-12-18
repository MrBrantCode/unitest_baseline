"""
QUESTION:
Classify a collection of articles as spam or ham based on multiple criteria. Implement a function `classify_articles` that takes a list of strings where each string represents an article and returns a list of classifications. The classification should be based on criteria such as presence of certain words or patterns, article length, and word frequency. 

The function should handle up to 100,000 articles in the input list, each with a maximum length of 2000 characters, and up to 100 unique words or patterns used for classification. The function should be able to handle the classification task in a reasonable amount of time.
"""

import re

def classify_articles(articles):
    classification = []
    spam_words = ["spam", "offer", "free", "amazing"]
    spam_patterns = [re.compile(r'\b\d{4}\b')]  
    
    for article in articles:
        contains_spam_words = any(word in article.lower() for word in spam_words)
        contains_spam_patterns = any(pattern.search(article) for pattern in spam_patterns)
        is_too_long = len(article) > 2000
        
        if contains_spam_words or contains_spam_patterns or is_too_long:
            classification.append("spam")
        else:
            classification.append("ham")
    
    return classification