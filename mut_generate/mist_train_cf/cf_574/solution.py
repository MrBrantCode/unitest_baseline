"""
QUESTION:
Write a function `find_longest_word` that takes a string sentence as input, where the sentence contains only alphabets and spaces. The function should find the longest word in the sentence and return the number of unique vowels in that word.
"""

def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return sum(1 for char in set(longest_word.lower()) if char in 'aeiou')