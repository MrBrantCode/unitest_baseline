"""
QUESTION:
Create a function called `count_occurrences` that takes a string as input. The function should return the number of occurrences of the word 'Python' (ignoring case) followed immediately by the word 'programming' (ignoring case) without any punctuation in between.
"""

def count_occurrences(string):
    words = string.replace(',', '').replace('.', '').split()
    count = 0
    for i in range(len(words) - 1):
        if words[i].lower() == 'python' and words[i + 1].lower() == 'programming':
            count += 1
    return count