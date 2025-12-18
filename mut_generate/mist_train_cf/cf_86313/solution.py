"""
QUESTION:
Write a function `count_vowels` that takes a string as input, converts it to lower case, counts the number of vowels, and returns the count. The input string may contain punctuation marks, special characters, and multiple spaces between words. The solution should have a time complexity of O(n) and a space complexity of O(1).
"""

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    string = string.lower()  # convert string to lower case

    for char in string:
        if char in vowels:
            count += 1

    return count