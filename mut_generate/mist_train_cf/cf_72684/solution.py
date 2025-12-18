"""
QUESTION:
Create a function named `check_anagram(s1, s2)` that takes two phrases `s1` and `s2` as input, ignores spaces and punctuation, and determines whether they are anagrams of each other. The function should return `True` if the phrases are anagrams and `False` otherwise.
"""

def check_anagram(s1, s2):
    # Removing punctuations, lowercasing and sorting 
    s1_clean = sorted(s1.lower().replace(' ', '').replace(',', '').replace('.', '')) 
    s2_clean = sorted(s2.lower().replace(' ', '').replace(',', '').replace('.', '')) 

    # Comparing these lists to check if they are equal
    return s1_clean == s2_clean