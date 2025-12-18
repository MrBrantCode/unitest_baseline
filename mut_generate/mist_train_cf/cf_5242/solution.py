"""
QUESTION:
Write a function `find_longest_string` that takes a string and two substrings as input and returns the length of the longest substring between the two given substrings. The function should be case-insensitive when searching for the substrings and only return the length of the substring if it is a prime number. If no such substring is found, the function should return 0.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_longest_string(string, start_substring, end_substring):
    string = string.lower()
    start_substring = start_substring.lower()
    end_substring = end_substring.lower()
    
    start_index = string.find(start_substring)
    if start_index == -1:
        return 0
    
    end_index = string.find(end_substring, start_index + len(start_substring))
    if end_index == -1:
        return 0
    
    found_string = string[start_index + len(start_substring):end_index]
    found_string_length = len(found_string)
    
    if is_prime(found_string_length):
        return found_string_length
    else:
        return 0