"""
QUESTION:
Write a function named `sort_by_length` that takes a list of words as input and returns a sorted list of words. The sorted list should only include words that start with a vowel ('a', 'e', 'i', 'o', 'u') and have more than 5 characters. The sorting order should be based on the length of the words and then their lexicographical order. The function should have a time complexity of O(n log n).
"""

def sort_by_length(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sorted(filter(lambda x: len(x) > 5 and x[0].lower() in vowels, words), key=lambda x: (len(x), x))