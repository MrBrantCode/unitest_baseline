"""
QUESTION:
Create a function named `extract_sort_reverse` that takes a list of strings as input where each string contains at least 3 words. The function should extract the first 4 characters from each word, sort the resulting list in alphabetical order, and return it in reverse order. If a word is less than 4 characters long, it should be excluded from the resulting list.
"""

def extract_sort_reverse(strings):
    extracted = [word[:4] for string in strings for word in string.split() if len(word) >= 4]
    return sorted(extracted)[::-1]