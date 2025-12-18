"""
QUESTION:
Create a function `shortest_string_without_vowels(s1, s2, s3)` that takes three distinct strings as parameters and returns the shortest string that strictly excludes any presence of vowel characters.
"""

def shortest_string_without_vowels(s1, s2, s3):
    vowels = set("aeiouAEIOU") 
    s1 = "".join(ch for ch in s1 if ch not in vowels)
    s2 = "".join(ch for ch in s2 if ch not in vowels)
    s3 = "".join(ch for ch in s3 if ch not in vowels)
    return min(s1, s2, s3, key=len)