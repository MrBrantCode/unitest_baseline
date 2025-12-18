"""
QUESTION:
Create a function named `classifyArticle` that takes a string as input and returns a string representing the topic category of the article, which can be "Politics", "Economy", "Tech", "Science", "Culture", "Education", "Sports", or "Lifestyle". The function should be case-insensitive, handle leading and trailing spaces, punctuation marks, multiple spaces, abbreviations, acronyms, special characters, numbers, and non-English words, without using external libraries or pre-built classification functions. If the input string does not match any topic category, return an empty string.
"""

def classifyArticle(article: str) -> str:
    # Remove leading and trailing spaces
    article = article.strip()
    
    # Convert the article to lowercase
    article = article.lower()
    
    # Remove punctuation marks
    article = ''.join(e for e in article if e.isalnum() or e.isspace())
    
    # Remove multiple spaces
    article = ' '.join(article.split())
    
    # Check if the article contains any of the topic keywords
    if "politics" in article:
        return "Politics"
    elif "economy" in article:
        return "Economy"
    elif "tech" in article or "technology" in article:
        return "Tech"
    elif "science" in article:
        return "Science"
    elif "culture" in article:
        return "Culture"
    elif "education" in article:
        return "Education"
    elif "sports" in article:
        return "Sports"
    elif "lifestyle" in article:
        return "Lifestyle"
    else:
        return ""