"""
QUESTION:
Write a function `vowel_analysis(s)` that takes a string `s` as input and returns the total number of vowels (both lowercase and uppercase) in the string.
"""

def vowel_analysis(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count