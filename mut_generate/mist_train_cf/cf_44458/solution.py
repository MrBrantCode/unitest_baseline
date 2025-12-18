"""
QUESTION:
Write a function `check_anagrams(str1, str2)` that checks if two input strings are anagrams, considering only alphanumeric characters and ignoring cases, without using built-in sorting functions.
"""

def check_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_list = [char for char in str1 if char.isalnum()]
    str2_list = [char for char in str2 if char.isalnum()]
    
    counter = [0]*256
    
    for char in str1_list:
        counter[ord(char)] += 1
    
    for char in str2_list:
        counter[ord(char)] -= 1
        
    for count in counter:
        if count != 0:
            return False
    
    return True