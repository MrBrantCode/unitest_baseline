"""
QUESTION:
Write a function `longestCommonSuffix(arr)` that takes a list of strings `arr` as input and returns the longest common suffix among them. The function should handle edge cases such as an empty list of strings, and provide an error handling mechanism for such cases. The function should be optimized for time sensitivity, especially for larger sizes of strings.
"""

from functools import reduce

def longestCommonSuffix(arr):
    if len(arr) == 0:
        return ""
        
    def commonSuffix(str1, str2):
        i = -1  
        while abs(i) <= min(len(str1),len(str2)):  
            if str1[i] != str2[i]:  
                return str1[i+1:]
            i -= 1  
        return str1[i+1:]
        
    return reduce(commonSuffix, arr)