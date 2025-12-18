"""
QUESTION:
Design a function named MostFrequentChar that takes a string as input and returns the character that appears most frequently. The function is case-sensitive, and in the event of a tie, it returns the first character that reaches the maximum frequency. The function should work for strings containing any kind of characters, including letters, digits, spaces, and punctuation.
"""

def MostFrequentChar(string):
    dictionary = {}
    for char in string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    values = list(dictionary.values())
    keys = list(dictionary.keys())
    return keys[values.index(max(values))]