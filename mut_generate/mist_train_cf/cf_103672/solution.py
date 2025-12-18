"""
QUESTION:
Write a function `classifyArticle` that takes a string `article` as input and returns the topic of the article, which can be one of the following 8 categories: "Politics", "Economy", "Tech", "Science", "Culture", "Education", "Sports", or "Lifestyle". The function should be able to correctly classify the article based on its content.
"""

def classifyArticle(article):
    topics = ["Politics", "Economy", "Tech", "Science", "Culture", "Education", "Sports", "Lifestyle"]
    keywords = {
        "Politics": ["government", "policy", "election", "president", "congress"],
        "Economy": ["market", "stock", "economy", "business", "trade"],
        "Tech": ["tech", "technology", "computer", "software", "hardware"],
        "Science": ["science", "research", "lab", "study", "discovery"],
        "Culture": ["culture", "art", "music", "film", "festival"],
        "Education": ["education", "school", "university", "student", "teacher"],
        "Sports": ["sports", "game", "player", "team", "championship"],
        "Lifestyle": ["lifestyle", "health", "food", "travel", "fashion"]
    }

    article = article.lower()
    max_matches = 0
    topic = ""

    for t in topics:
        matches = sum(1 for k in keywords[t] if k in article)
        if matches > max_matches:
            max_matches = matches
            topic = t

    return topic