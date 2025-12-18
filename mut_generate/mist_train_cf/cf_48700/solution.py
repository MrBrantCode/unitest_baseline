"""
QUESTION:
Implement a function named `sort_alphabets` that takes a list of characters as input and returns the list sorted in ascending alphabetical order. The function must not use any pre-existing sorting algorithms or techniques, and should be able to sort the list manually.
"""

def sort_alphabets(alphabets):
    n = len(alphabets)

    for i in range(n):
        for j in range(0, n-i-1):
            if alphabets[j] > alphabets[j+1] :
                alphabets[j], alphabets[j+1] = alphabets[j+1], alphabets[j]

    return alphabets