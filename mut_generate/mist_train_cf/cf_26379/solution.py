"""
QUESTION:
Implement a function `count_comment_words` that takes a multi-line string `input_str` as input, extracts all comments starting with `#`, splits these comments into unique words, and returns a dictionary where the keys are the unique words and the values are their respective counts. The function should consider each word as a sequence of alphanumeric characters or non-ASCII characters separated by non-alphanumeric characters. The input string may contain Python code snippets and the function should ignore non-comment lines.
"""

import re

def count_comment_words(input_str: str) -> dict:
    comments = re.findall(r'#.*', input_str)
    word_count = {}
    for comment in comments:
        words = re.findall(r'\w+', comment)
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count