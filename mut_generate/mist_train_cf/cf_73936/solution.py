"""
QUESTION:
Create a function `least_frequent_last(s)` that finds the least frequent letter in a given string `s` of lowercase alphabets. If two or more letters have the same frequency, return the one that occurs last in the string. The function should disregard spaces and special characters.
"""

def least_frequent_last(s):
    counts = {}
    for char in s:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    
    least_frequent = min(counts, key=counts.get)
    for char in reversed(s):
        if char.isalpha() and counts[char] == counts[least_frequent]:
            return char
    
    return least_frequent