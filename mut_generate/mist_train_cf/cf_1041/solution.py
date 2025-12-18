"""
QUESTION:
Write a function `reverse_vowels` that takes a string as input and returns the string with the order of vowels reversed, maintaining the original case. The input string may contain both uppercase and lowercase characters.
"""

def reverse_vowels(s):
    vowels = "AEIOUaeiou"
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return ''.join(s)