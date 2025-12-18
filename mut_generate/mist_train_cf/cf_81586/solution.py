"""
QUESTION:
Write a function `anagram_checker` that takes two strings as input, determines if they are anagrams of each other, and returns the number of distinct anagrams that can be formed from each string. The function should ignore spaces, punctuation, and capitalization in its evaluation.
"""

from collections import Counter
import math

def anagram_checker(str1, str2):
    str1 = str1.lower().replace(" ", "").replace(",", "").replace(".", "")
    str2 = str2.lower().replace(" ", "").replace(",", "").replace(".", "")
    
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    
    anagrams_str1 = math.factorial(len(str1))
    for letter in counter1:
        anagrams_str1 //= math.factorial(counter1[letter])
        
    anagrams_str2 = math.factorial(len(str2))
    for letter in counter2:
        anagrams_str2 //= math.factorial(counter2[letter])
        
    return counter1 == counter2, anagrams_str1, anagrams_str2