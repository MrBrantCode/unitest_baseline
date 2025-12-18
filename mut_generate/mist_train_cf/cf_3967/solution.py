"""
QUESTION:
Write a function `count_occurrences` that takes a string as input and returns the number of occurrences of 'Python' (ignoring case) followed by 'programming' (ignoring case) without any punctuation in between.
"""

def count_occurrences(string):
    words = string.replace(',', '').split()
    count = 0
    for i in range(len(words) - 1):
        if words[i].lower() == 'python' and words[i + 1].lower() == 'programming':
            count += 1
    return count