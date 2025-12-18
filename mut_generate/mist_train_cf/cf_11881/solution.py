"""
QUESTION:
Write a function `find_longest_substring` that takes a string as input and returns the longest substring that starts with a vowel and has no repeating characters. The function should only consider the English vowels 'a', 'e', 'i', 'o', and 'u'.
"""

def find_longest_substring(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    longest_substring = ""
    for i in range(len(string)):
        if string[i] in vowels:
            current_substring = string[i]
            for j in range(i + 1, len(string)):
                if string[j] in current_substring:
                    break
                current_substring += string[j]
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
    return longest_substring