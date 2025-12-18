"""
QUESTION:
Write a function named `find_longest_vowel_substring` that takes a string `s` as input and returns the maximum number of consecutive vowels and the corresponding substring. The function should have a time complexity of O(n^2) and should not use any built-in string manipulation functions or regular expressions.
"""

def find_longest_vowel_substring(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_count = 0
    max_substring = ""
    n = len(s)
    
    for i in range(n):
        count = 0
        substring = ""
        for j in range(i, n):
            if s[j].lower() in vowels:
                count += 1
                substring += s[j]
            else:
                break
            
            if count > max_count:
                max_count = count
                max_substring = substring
    
    return max_count, max_substring