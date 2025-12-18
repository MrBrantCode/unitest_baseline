"""
QUESTION:
Write a function `count_vowels(string)` that takes a string as input, converts it to lower case, and returns the number of vowels in the string. The input string can contain punctuation marks, special characters, and multiple spaces between words. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    string = string.lower()  # convert string to lower case

    for char in string:
        if char in vowels:
            count += 1

    return count