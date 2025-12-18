"""
QUESTION:
Design a function `count_vowel_frequency(input_str)` to find the frequency of occurrence of each vowel in a given string `input_str`. The input string can contain uppercase and lowercase letters, digits, special characters, and spaces, and can have a maximum length of 10^6 characters. The function should not use any built-in functions or libraries for string manipulation or regular expressions. The algorithm should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def count_vowel_frequency(input_str):
    vowelFreq = [0] * 5
    input_str = input_str.lower()

    for ch in input_str:
        if ch == 'a':
            vowelFreq[0] += 1
        elif ch == 'e':
            vowelFreq[1] += 1
        elif ch == 'i':
            vowelFreq[2] += 1
        elif ch == 'o':
            vowelFreq[3] += 1
        elif ch == 'u':
            vowelFreq[4] += 1

    return vowelFreq