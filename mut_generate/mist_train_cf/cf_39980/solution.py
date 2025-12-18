"""
QUESTION:
Write a function `reverseVowels` to reverse only the vowels in a given string. The vowels are 'a', 'e', 'i', 'o', 'u', and they can be in both uppercase and lowercase. The input string length is between 1 and 10^5 characters. The function should return the string after reversing the vowels.
"""

def reverseVowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        while s[left] not in vowels and left < right:
            left += 1
        while s[right] not in vowels and left < right:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)