"""
QUESTION:
Given a string, write a function `longest_twin_palindrome` that finds the longest segment within the string that forms a palindrome and has the same character at both ends. The function should return this longest twin palindrome segment.
"""

def longest_twin_palindrome(textual_fragment):
    max_length = 0
    start = 0
    for i in range(len(textual_fragment)):
        for j in range(i + max_length, len(textual_fragment)):
            segment = textual_fragment[i:j + 1]
            if segment == segment[::-1] and segment[0] == segment[-1]:
                length = len(segment)
                if length > max_length:
                    max_length = length
                    start = i
    return textual_fragment[start:start + max_length]