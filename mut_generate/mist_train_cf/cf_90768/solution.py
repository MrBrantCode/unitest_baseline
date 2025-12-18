"""
QUESTION:
Implement a function named `classify_articles` that takes two parameters: a list of strings representing articles and a list of strings representing spam patterns. The function should return a list of classifications, where each classification is either "spam" or "ham", based on the presence of spam patterns in the articles. The function should be able to handle up to 100,000 articles and 100 unique spam patterns, with each article having a maximum length of 1000 characters.
"""

def classify_articles(articles, spam_patterns):
    result = []
    for article in articles:
        is_spam = False
        for pattern in spam_patterns:
            if pattern.lower() in article.lower():
                result.append("spam")
                is_spam = True
                break
        if not is_spam:
            result.append("ham")
    return result