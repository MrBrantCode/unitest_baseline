"""
QUESTION:
Create a function `count_alphabet_frequency(input_string)` that takes an input string and returns a dictionary where the keys are the unique alphabets (both lowercase and uppercase) present in the input string, and the values are the frequency of each alphabet. The function should be case-insensitive and ignore non-alphabet characters such as spaces, special characters, and numbers.
"""

def count_alphabet_frequency(input_string):
    frequency = {}
    input_string = input_string.lower()
    for char in input_string:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency