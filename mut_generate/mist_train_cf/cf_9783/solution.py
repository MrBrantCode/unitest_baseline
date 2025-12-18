"""
QUESTION:
Write a function `count_vowels` that takes a string as input and returns a dictionary containing the count of each vowel (a, e, i, o, u) in the string. The function must have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
"""

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in string:
        if char.lower() in vowels:
            count[char.lower()] += 1
    return count