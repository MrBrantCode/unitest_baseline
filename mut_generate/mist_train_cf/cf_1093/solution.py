"""
QUESTION:
Create a function `count_unique_vowels` that takes a string as input and returns the number of unique vowels in the string, ignoring whitespace characters and treating uppercase and lowercase vowels as different characters. The function should have a time complexity of O(n), where n is the length of the string, and should not use the `len()` function.
"""

def count_unique_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    seen = set()
    
    for char in s:
        if char.isalpha() and char.lower() in vowels and char not in seen:
            count += 1
            seen.add(char)
    
    return count