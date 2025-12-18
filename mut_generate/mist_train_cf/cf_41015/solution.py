"""
QUESTION:
Write a function `reverse_vowels(name: str) -> str` that takes a string of lowercase letters and returns the modified string with the vowels 'a', 'e', 'i', 'o', and 'u' reversed while keeping the consonants in their original positions.
"""

def reverse_vowels(name: str) -> str:
    vowels = set('aeiou')
    name_list = list(name)
    left, right = 0, len(name_list) - 1

    while left < right:
        while name_list[left] not in vowels and left < right:
            left += 1
        while name_list[right] not in vowels and left < right:
            right -= 1
        name_list[left], name_list[right] = name_list[right], name_list[left]
        left += 1
        right -= 1

    return ''.join(name_list)