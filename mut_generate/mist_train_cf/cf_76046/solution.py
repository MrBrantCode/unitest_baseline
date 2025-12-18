"""
QUESTION:
Write a function called `longest_palindrome_substring` that takes a string `s` as input and returns the longest repeated substring that is also symmetrical (a palindrome) within `s`. The input string will contain only lowercase letters and no spaces. The function should return "No repeated palindrome found" if no repeated palindrome is found.
"""

def longest_palindrome_substring(s):
    n = len(s) 
    substring_set = set([s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)])
    palindrome_set = [sub for sub in substring_set if sub == sub[::-1]]
    count_dict = {pal: s.count(pal) for pal in palindrome_set if s.count(pal) > 1}
    if count_dict:
        max_key = max(count_dict, key=lambda k: len(k))
        return max_key
    else:
        return "No repeated palindrome found"