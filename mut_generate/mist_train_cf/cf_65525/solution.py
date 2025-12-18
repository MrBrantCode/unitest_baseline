"""
QUESTION:
Write a function `check_anagrams(s1, s2)` that checks if two input strings `s1` and `s2` are anagrams of each other. The function should not use any built-in or sorting functions, and it must consider case sensitivity. The solution must achieve linear time complexity, i.e., O(n).
"""

def check_anagrams(s1, s2):
    counter = {}
    
    for letter in s1:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    
    for letter in s2:
        if letter in counter:
            counter[letter] -= 1
        else:
            return False   # If the letter in s2 is not present in s1, then they are not anagrams.
            
    for key in counter:
        if counter[key] != 0:
            return False   # If the count of any letter is not 0 after checking both strings, then they are not anagrams.
    
    return True  # If the count of every letter is 0, then they are anagrams.