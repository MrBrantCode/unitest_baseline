"""
QUESTION:
Write a function `find_subsequence_index(string, num)` that finds the index of the first occurrence of a specific subsequence of characters represented by the integer in the string. The subsequence should consist of the digits in the integer concatenated in ascending order. Return -1 if the subsequence is not found. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in functions or methods for string manipulation or external libraries.
"""

def find_subsequence_index(string, num):
    digits = [int(d) for d in str(num)]
    i = 0
    j = 0
    
    while i < len(string) and j < len(digits):
        if string[i] == str(digits[j]):
            i += 1
            j += 1
        else:
            i += 1
    
    if j == len(digits):
        return i - len(digits)
    else:
        return -1