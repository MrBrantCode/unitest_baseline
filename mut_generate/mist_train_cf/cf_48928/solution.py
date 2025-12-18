"""
QUESTION:
Create a function `custom_histogram` that takes a string of space-separated letters (case insensitive) as input. The function should return a dictionary where keys are the letters in lowercase followed by their counts (e.g., 'a_1', 'b_2') and values are the corresponding counts. The function should disregard special characters and include all letters with the maximum frequency in the output. If the input string is empty, the function should return an empty dictionary.
"""

def custom_histogram(s):
    from collections import Counter
    import re

    s = re.sub(r'[^A-Za-z\s]', '', s)
    counter = Counter(s.lower().split())

    result = {}
    for letter, count in counter.items():
        result[letter + "_" + str(count)] = count

    max_count = max(counter.values(), default=0)
    result = {k: v for k, v in result.items() if v == max_count}

    return result