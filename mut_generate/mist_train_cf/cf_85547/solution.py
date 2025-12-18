"""
QUESTION:
Implement the following three functions: `is_palindrome`, `make_palindrome`, and `most_common`. 

Function `is_palindrome` should return a boolean value that determines if the provided string is a palindrome, ignoring case, non-alphanumeric characters, and spaces.

Function `make_palindrome` should determine the minimum number of characters needed to be appended at the end of the string to make it a palindrome. To achieve this, it should: 
1. Find the longest palindrome suffix of the string.
2. Calculate the length of string prefix before the palindrome suffix.
3. Return the length of the prefix as the minimum number of characters needed to create the shortest possible palindrome.

Function `most_common` should find the most common character in the string. If two or more characters occur the same maximum amount of time, return any one of them.

No external modules or libraries can be used.
"""

def is_palindrome(string):
    string = ''.join(char.lower() for char in string if char.isalnum())
    return string == string[::-1]

def make_palindrome(string):
    string = ''.join(char.lower() for char in string if char.isalnum())
    suffix_length = len(string)
    while suffix_length > 0 and string[:suffix_length] != string[:suffix_length][::-1]:
        suffix_length -= 1
    return len(string) - suffix_length

def most_common(string):
    string = ''.join(char.lower() for char in string if char.isalnum())
    char_frequency = {}
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    max_frequency = max(char_frequency.values())
    for char, frequency in char_frequency.items():
        if frequency == max_frequency:
            return char