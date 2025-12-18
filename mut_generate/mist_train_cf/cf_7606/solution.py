"""
QUESTION:
Write a function `longest_vowel_string(strings)` that takes an array of lowercase strings as input and returns the longest string that starts with a vowel and has a length greater than 3 and contains at least one consecutive pair of identical characters. If no such string exists, return an empty string. The input array will have at most 1000 elements.
"""

def longest_vowel_string(strings):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    longest_string = ""
    
    for string in strings:
        if len(string) > 3 and string[0] in vowels:
            for i in range(len(string) - 1):
                if string[i] == string[i+1]:
                    if len(string) > len(longest_string):
                        longest_string = string
                    break
    
    return longest_string