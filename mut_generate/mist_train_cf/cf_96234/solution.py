"""
QUESTION:
Create a function `replaceAndSort(words)` that takes an array of words, replaces non-alphabet characters, converts to lowercase, replaces each character with its corresponding number from the English alphabet (a=1, b=2...z=26), computes the sum of each word, and returns the array sorted in ascending order based on these sums. Each word will have at most 10 characters and the array will have at most 100 words.
"""

def replaceAndSort(words):
    def computeSum(word):
        word = ''.join(filter(str.isalpha, word.lower()))
        return sum(ord(c) - ord('a') + 1 for c in word)
    return sorted(words, key=computeSum)