"""
QUESTION:
Write a function `is_palindrome` that determines if a given set of strings is a palindrome. The strings in the set are composed of only lowercase English alphabets and the maximum length of each string is 100. The palindrome test should be case-insensitive. The function should return a boolean value indicating whether the set is a palindrome. The time complexity of the function should be O(n), where n is the total number of characters in all the strings in the set.
"""

def is_palindrome(s):
    normalized_strings = []
    for string in s:
        normalized_strings.append(string.lower())
    
    combined_string = ''.join(normalized_strings)
    start = 0
    end = len(combined_string) - 1
    
    while start <= end:
        if combined_string[start] != combined_string[end]:
            return False
        start += 1
        end -= 1
    
    return True