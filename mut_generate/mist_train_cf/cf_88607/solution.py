"""
QUESTION:
Write a function `is_isogram(s)` that determines if a given string `s` is an isogram, considering both uppercase and lowercase letters, and ignoring special characters and spaces. The function should return a tuple where the first element is a boolean indicating whether the string is an isogram and the second element is a dictionary containing the count of each letter in the string. The function should have a time complexity of O(n) and should not use any additional data structures beyond a single dictionary.
"""

def is_isogram(s):
    char_count = {}
    for char in s.lower():  
        if char.isalpha():  
            if char in char_count:  
                return False
            char_count[char] = char_count.get(char, 0) + 1
    return True, char_count