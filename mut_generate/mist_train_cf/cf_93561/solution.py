"""
QUESTION:
Write a function `longest_consecutive_sequence` that takes a string as input and returns the longest consecutive sequence of characters that does not contain any vowels. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def longest_consecutive_sequence(my_string):
    max_len = 0
    curr_len = 0
    start = -1
    end = -1
    vowels = "aeiou"

    for i, c in enumerate(my_string):
        if c in vowels:
            curr_len = 0
        else:
            if curr_len == 0:
                start = i
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
                end = i

    return my_string[start:end+1]