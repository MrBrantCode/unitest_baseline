"""
QUESTION:
Write a function named count_lowercase() that takes a string as input and returns the total number of lowercase characters that are not immediately preceded or followed by an uppercase character. The function should not use the built-in functions islower(), isupper(), and index().
"""

def count_lowercase(string):
    total = 0
    for i in range(len(string)):
        if ord('a') <= ord(string[i]) <= ord('z') and ((i == 0 or ord('a') <= ord(string[i-1]) <= ord('z')) and (i == len(string)-1 or ord('a') <= ord(string[i+1]) <= ord('z'))):
            total += 1
    return total