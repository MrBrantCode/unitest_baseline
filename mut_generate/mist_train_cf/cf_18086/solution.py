"""
QUESTION:
Write a function `letter_frequency_distribution` that takes a string as input and returns a dictionary with the frequency distribution of the letters in the string. The function should exclude special characters, numbers, and whitespace from the frequency distribution, and handle uppercase and lowercase letters as separate entities. The time complexity should be O(n) and the space complexity should be O(1), where n is the length of the input string.
"""

def letter_frequency_distribution(string):
    frequency = {}

    for char in string:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1

    return frequency