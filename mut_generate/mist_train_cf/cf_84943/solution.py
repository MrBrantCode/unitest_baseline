"""
QUESTION:
Create a function named `check_anagram` that takes two string parameters, `str1` and `str2`, and returns `True` if they are anagrams of each other (contain the same characters, regardless of order), and `False` otherwise.
"""

def check_anagram(str1, str2): 
    sorted_str1 = sorted(str1) 
    sorted_str2 = sorted(str2)
  
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False