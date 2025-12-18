"""
QUESTION:
Implement a function named `sort_words` that takes a list of words as input, sorts them in lexicographical order, and returns a set of unique words in lowercase. If two words have the same length, they should be sorted based on their ASCII values. The function should have a time complexity of O(nlogn) and a space complexity of O(1), and it cannot use any built-in sorting functions or libraries.
"""

def sort_words(words):
    words = [word.lower() for word in words]
    n = len(words)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if words[i] > words[i + 1] or (len(words[i]) == len(words[i + 1]) and words[i] > words[i + 1]):
                words[i], words[i + 1] = words[i + 1], words[i]
                swapped = True

    unique_words = set(words)
    return unique_words