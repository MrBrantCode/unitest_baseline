"""
QUESTION:
Write a function `filter_and_group_chars` that takes a string `text` as input and returns a string containing the consonants in `text`, grouped by their frequency in descending order. The function should exclude digits, special characters, and whitespace characters from the output and ignore letter case.
"""

def filter_and_group_chars(text):
    from collections import Counter
    import re

    text = re.sub(r'\W|\d|\s', '', text)  # Remove digits and special characters
    text = text.lower()  # Convert to lowercase
    counter = Counter(text)
    sorted_keys = sorted(counter.keys(), key=lambda x: (-counter[x], x))
    return "".join([key * counter[key] for key in sorted_keys if key not in 'aeiou'])