"""
QUESTION:
Write a function `reverse_string(s, index)` that takes a string `s` and an index as input and prints the characters of `s` in reverse order without using any pre-existing functions or iterative constructs. The additional space used should not exceed O(1).
"""

def reverse_string(s, index):
    if index == -1:
        return
    print(s[index], end='')
    reverse_string(s, index-1)