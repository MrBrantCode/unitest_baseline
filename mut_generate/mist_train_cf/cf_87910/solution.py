"""
QUESTION:
Create a function `filter_keywords(text, keywords)` that takes two inputs: a string `text` of length `n` containing only alphabetical characters and spaces, and a list of `m` strings `keywords`, each of length `k`. 

Return a new string formed by removing all occurrences of the keywords from the input text. The function should handle case-insensitive matching of keywords and remove partial matches of keywords embedded within other words. The output string should maintain the same case as the input text. 

The function should have a time complexity of O(n * m * k) and a space complexity of O(n).
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