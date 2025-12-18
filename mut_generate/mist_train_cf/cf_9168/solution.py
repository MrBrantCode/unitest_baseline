"""
QUESTION:
Implement a function `classify_articles` that takes a list of article strings and a list of spam patterns as input. The function should classify each article as "spam" if it contains any of the spam patterns (case-insensitive search) and "ham" otherwise. The function should be able to handle up to 100,000 articles, each with a maximum length of 1000 characters, and up to 100 unique spam patterns. Return a list of classifications for the input articles.
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