"""
QUESTION:
Create a function `longest_consecutive_uppercase` that takes a string as input and returns the longest consecutive sequence of characters that are all uppercase letters, excluding vowels. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def longest_consecutive_uppercase(string):
    max_len = 0
    curr_len = 0
    max_start = 0
    curr_start = 0
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    for i in range(len(string)):
        if string[i].isupper() and string[i] not in vowels:
            curr_len += 1
            if curr_len == 1:
                curr_start = i
            if curr_len > max_len:
                max_len = curr_len
                max_start = curr_start
        else:
            curr_len = 0
    
    return string[max_start: max_start + max_len]