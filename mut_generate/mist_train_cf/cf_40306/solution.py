"""
QUESTION:
Implement a function called `tokenize_string` that takes an `input_string` and a list of `keywords` as input. The function should find all occurrences of the `keywords` in the `input_string`, and return a list of tuples where each tuple contains a `keyword` and its corresponding position in the `input_string`. The position is the index of the first character of the `keyword` in the `input_string`. The function should be case-sensitive and return the positions in the order of their appearance in the `input_string`.
"""

def tokenize_string(input_string, keywords):
    tokens = []
    for keyword in keywords:
        start = 0
        while True:
            start = input_string.find(keyword, start)
            if start == -1:
                break
            tokens.append((keyword, start))
            start += len(keyword)
    return tokens