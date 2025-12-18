"""
QUESTION:
Create a function named `CharacterFrequencyCounter` that calculates the frequency of alphabetic characters in a given string, ignoring non-alphabetic characters and considering 'a' and 'A' as the same character. The function should have a time complexity of O(n) and a space complexity of O(26). The output should be a dictionary where keys are unique alphabets and values are their frequencies. The function should handle unicode characters and large input strings efficiently.
"""

def CharacterFrequencyCounter(input_string):
    frequency = {}
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency