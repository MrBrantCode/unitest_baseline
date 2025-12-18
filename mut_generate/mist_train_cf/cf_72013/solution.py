"""
QUESTION:
Write a Python function `abusive_words` that takes a list of text lines as input and returns the total count of occurrences of predefined offensive words and a list of line numbers where these words appear. The function should be able to handle large datasets efficiently.

The predefined list of offensive words is `['stupid', 'jerk', 'moron']`. The input list of text lines can contain thousands or millions of lines.

Additionally, write a separate Python function `cleaner` that takes a text line and the list of predefined offensive words as input, and returns the text line with all occurrences of the offensive words replaced with '****'.
"""

def abusive_words(words):
    word_list = ['stupid', 'jerk', 'moron']
    count = 0
    lines = []
    for i, line in enumerate(words, start=1):
        for word in word_list:
            if word in line:
                count += 1
                if i not in lines:
                    lines.append(i)
    return count, lines

def cleaner(text, word_list):
    for word in word_list:
        text = text.replace(word, '****')
    return text