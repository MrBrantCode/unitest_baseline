"""
QUESTION:
Reverse a string without using any built-in functions or libraries. The input string consists of uppercase and lowercase letters and may contain leading or trailing spaces. The reversed string should maintain the same case as the original string. Implement a solution with a time complexity of O(n) and a space complexity of O(1). The function should take one parameter, the input string.
"""

def reverse_string(s):
    s = list(s)
    start, end = 0, len(s) - 1

    while start <= end:
        if s[start] == ' ':
            start += 1
            continue
        if s[end] == ' ':
            end -= 1
            continue
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    return ''.join(s)