"""
QUESTION:
Write a function named `reverse_vowels` that takes a string as input and returns a new string where the vowels appear in reverse order. The function should handle both lowercase and uppercase vowels and keep non-vowel characters at their original positions.
"""

def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    left, right = 0, len(s) - 1
    s = list(s)

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