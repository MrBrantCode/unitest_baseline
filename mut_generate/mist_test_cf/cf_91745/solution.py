"""
QUESTION:
Create a function `filter_keywords(text, keywords)` that filters out keywords from a given text. The function should take a string `text` and a list of strings `keywords` as input, and return a new string that is formed by removing all occurrences of the keywords from the input text, preserving their order. The function should have a time complexity of O(n * m * k) and a space complexity of O(n), where n is the length of the text, m is the number of keywords, and k is the maximum length of a keyword.
"""

def filter_keywords(text, keywords):
    keyword_set = set(keywords)
    filtered_text = []
    word = ""
    for char in text:
        if char.isalpha():
            word += char
        else:
            if word:
                if word not in keyword_set:
                    filtered_text.append(word)
                word = ""
            filtered_text.append(char)
    if word and word not in keyword_set:
        filtered_text.append(word)
    return "".join(filtered_text)