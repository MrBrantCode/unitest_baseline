"""
QUESTION:
Create a function named `filter_keywords` that takes two parameters: `text` and `keywords`. The function should return a new string that is formed by removing all occurrences of the keywords from the input text, with case-insensitive matching and handling of partial matches of keywords and embedded keywords within other words. The time complexity should be O(n * m * k) and the space complexity should be O(n), where n is the length of the input text, m is the number of keywords, and k is the length of each keyword.
"""

def filter_keywords(text, keywords):
    lowercase_keywords = set(keyword.lower() for keyword in keywords)
    words = text.split()
    filtered_words = []
    
    for word in words:
        lowercase_word = word.lower()
        should_filter = any(keyword in lowercase_word for keyword in lowercase_keywords)
        
        if not should_filter:
            filtered_words.append(word)
            
    filtered_text = ' '.join(filtered_words)
    return filtered_text