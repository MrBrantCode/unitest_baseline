"""
QUESTION:
Implement a function `bubble_sort_descending(words)` that sorts a list of words in descending order of word length using the bubble sort algorithm. The length of each word in the list is limited to 50 characters. The function should return the sorted list of words.
"""

def bubble_sort_descending(words):
    n = len(words)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if len(words[j]) < len(words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]
    return words