"""
QUESTION:
Write a function `find_closest_vowel_subsequence(word)` that extracts the closest vowel or vowel combination which forms one single sound, found between two consonants in a word, starting from the right side of the word. The function is case sensitive and must not consider vowels at the start and end of the word. If no such criteria is met, the function should return an empty string. Assume that the input word consists of English letters only. The function should also consider vowel combinations that form one single sound, such as "ea" in "heart".
"""

def find_closest_vowel_subsequence(word):
    vowels = 'aeiouAEIOU'
    result = ""
    vowel_flag = False 
    for letter in reversed(word):
        if letter in vowels:
            result = letter + result
            vowel_flag = True
        elif vowel_flag: 
            break
    if len(result) == len(word) or len(result) == 1: 
        return ""
    else:
        return result