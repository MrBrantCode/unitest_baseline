"""
QUESTION:
Write a function `count_alphabets(string)` that takes a string as input and returns a tuple. The first element of the tuple is the number of distinct alphabets in the string, and the second element is a dictionary where keys are the distinct alphabets and values are their corresponding frequencies. The function should be case-insensitive and ignore non-alphabet characters.
"""

def count_alphabets(string):
    string = string.lower()
    alphabet_count = {}
    for char in string:
        if char.isalpha():
            if char in alphabet_count:
                alphabet_count[char] += 1
            else:
                alphabet_count[char] = 1
    return len(alphabet_count), alphabet_count