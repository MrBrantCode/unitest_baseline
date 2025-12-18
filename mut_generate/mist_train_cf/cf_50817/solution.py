"""
QUESTION:
Create a function `vowels_count(s)` that takes a string `s` as input and returns the count of vowels in the string. Consider 'a', 'e', 'i', 'o', 'u' as vowels in any position and 'y' as a vowel only when it is at the end of the string. The function should disregard the case of the input string and handle special characters and non-string inputs correctly.
"""

def vowels_count(s):
    if not isinstance(s, str):
        return "Input must be a string"
    
    vowels = "aeiou"
    s = s.lower()
    count = sum([s.count(vowel) for vowel in vowels])
    
    if s and s[-1] == "y":
        count += 1
    
    return count