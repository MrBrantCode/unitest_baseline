"""
QUESTION:
Write a function `vowel_frequency` that takes a list of distinct words as input and returns a new list containing the frequency of vowel appearances within each individual word. The function should consider both lowercase and uppercase vowels (a, e, i, o, u).
"""

def vowel_frequency(words):
    vowel_frequency_list = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in words:
        vowel_count = 0
        for char in word:
            if char.lower() in vowels:
                vowel_count += 1
        vowel_frequency_list.append(vowel_count)
    return vowel_frequency_list