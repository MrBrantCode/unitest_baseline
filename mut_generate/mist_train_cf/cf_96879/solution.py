"""
QUESTION:
Write a function named `count_vowels` that calculates the frequency of occurrence of each vowel in a given string. The input string can contain uppercase and lowercase letters and is limited to a maximum length of 10^6 characters. The function should not use any built-in functions or libraries for string manipulation or regular expressions. The output should be a dictionary where the keys are the vowels ('a', 'e', 'i', 'o', 'u') and the values are their corresponding frequency counts.
"""

def count_vowels(string):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for char in string:
        char = char.lower()
        if char in vowels:
            vowels[char] += 1
    
    return vowels