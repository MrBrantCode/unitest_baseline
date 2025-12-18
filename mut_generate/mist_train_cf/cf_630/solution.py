"""
QUESTION:
Implement a function named `reverse_string` that takes a single string parameter and returns the input string with its characters reversed. The function should have a time complexity of O(n), where n is the length of the string, and a constant space complexity. The function should handle strings containing uppercase and lowercase letters, special characters, unicode characters, numbers, and leading or trailing whitespace. The function should preserve the case of each character in the reversed string.
"""

def reverse_string(s):
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

    return ''.join(s)