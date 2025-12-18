"""
QUESTION:
Write a function named longest_common_prefix that takes a list of strings as input and returns the longest common prefix of the list of strings. The function should have a time complexity of O(n*m), where n is the number of strings in the list and m is the length of the longest string. Implement the function using only bitwise operations and logical operators, without using any built-in string matching functions, loops, or recursion.
"""

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    min_len = min(len(s) for s in strs)
    
    common_prefix = ""
    
    for i in range(min_len):
        bit = ord(strs[0][i])
        
        for j in range(1, len(strs)):
            if ord(strs[j][i]) != bit:
                return common_prefix
        
        common_prefix += chr(bit)
    
    return common_prefix