"""
QUESTION:
Create a function named `manipulate_words(words, pattern)` that takes two parameters: a string of space-separated words and a string of space-separated integers representing a pattern. Each integer in the pattern corresponds to the position of a word in the input string. Implement the function to replace the pattern integers with the corresponding words from the input string and return the resulting string followed by "?!?".

Restrictions: The function should assume that the input words and pattern are valid and that the integers in the pattern are within the range of the number of input words.
"""

def entrance(words, pattern):
    words = words.split()
    pattern = list(map(int, pattern.split()))
    manipulated_string = ' '.join(words[i-1] for i in pattern)
    return manipulated_string + "?!?"