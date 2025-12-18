"""
QUESTION:
Create a function called `filter_keywords` that takes two parameters: `text` and `keywords`. The function should remove all occurrences of the keywords from the input text and return the resulting string. The input text is a string of length n containing only alphabetical characters and spaces, and the keywords are a list of m strings, each of length k. The function should have a time complexity of O(n * m * k) and a space complexity of O(n).
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