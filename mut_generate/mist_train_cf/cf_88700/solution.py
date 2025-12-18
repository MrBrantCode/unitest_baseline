"""
QUESTION:
Implement a function `count_frequency` to calculate the frequency of alphabets in a given input string, ignoring non-alphabet characters and considering 'a' and 'A' as the same character. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1) or O(26). The function should not use any built-in functions or libraries for counting the frequency of characters and should handle unicode characters and very large input strings efficiently.

The function should return a dictionary where the keys are the unique alphabets present in the input string and the values are the frequency of each alphabet.
"""

def count_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency