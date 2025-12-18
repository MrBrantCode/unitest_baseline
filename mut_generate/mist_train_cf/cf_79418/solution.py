"""
QUESTION:
Implement a function `anagram_of_palindrome` that takes a string `test_str` as input and returns a boolean value. The function should determine whether `test_str` is an anagram of any palindrome, ignoring white spaces and case sensitivity. The function should return True if `test_str` can be rearranged into a palindrome, and False otherwise.
"""

def anagram_of_palindrome(test_str):
    # Removing white spaces and converting to lower case
    test_str = test_str.replace(' ', '').lower()
    
    # Checking the count of each character
    char_count = {}
    for char in test_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # A string can form a palindrome if at most one character occurs odd number of times        
    odd_count_chars = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count_chars += 1
        if odd_count_chars > 1:
            return False
            
    return True