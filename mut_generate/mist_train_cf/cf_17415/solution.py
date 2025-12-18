"""
QUESTION:
Create a function named `count_words` that takes two parameters: a string `text` and a list `stop_words`. The function should return a dictionary where the keys are the words in the text (converted to lowercase, excluding the stop words) and the values are their corresponding frequency counts. The function should also be able to handle user-inputted lists of stop words.
"""

def count_words(text, stop_words):
    word_count = {}
    words = text.lower().split()
    for word in words:
        if word not in stop_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count