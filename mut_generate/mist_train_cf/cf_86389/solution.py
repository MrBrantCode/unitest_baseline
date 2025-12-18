"""
QUESTION:
Write a function named `sort_words` that takes a list of words as input and returns a set of unique words in lexicographical order, ensuring that words with the same length are sorted based on their ASCII values. The function should not use any built-in sorting functions or libraries, and it should convert all words to lowercase.
"""

def sort_words(words):
    words = [word.lower() for word in words]
    n = len(words)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if (len(words[i]), words[i]) > (len(words[i + 1]), words[i + 1]):
                words[i], words[i + 1] = words[i + 1], words[i]
                swapped = True

    return set(words)