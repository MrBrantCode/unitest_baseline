"""
QUESTION:
Write a function `count_characters` that takes a string of up to 10^6 characters consisting of lowercase letters, numbers, and special characters as input. The function should return a dictionary where the keys are the unique characters in the string and the values are their respective counts. The function should have a time complexity of O(n) and a space complexity of O(k), where n is the length of the input string and k is the number of unique characters in the string.
"""

def count_characters(string):
    char_count = {}
    
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count