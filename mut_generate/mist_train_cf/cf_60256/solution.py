"""
QUESTION:
Write a function `longest_common_suffix` that takes a list of strings as input and returns the longest common suffix among all the strings in the list. If the input list is empty, return an empty string. If there is no common suffix, return the string "No common suffix". The function should optimize for time complexity.
"""

def longest_common_suffix(strs):
    if not strs:
        return ""
    
    # Sort the array
    strs.sort()
    
    # Compare the first and last string character by character
    # Since the array is sorted, the common suffix of first and last string will be the longest common suffix.
    first = strs[0]
    last = strs[-1]
    
    i = 0
    while i < len(first) and i < len(last) and first[-i-1] == last[-i-1]:
        i += 1
        
    return first[-i:][::-1] if i > 0 else "No common suffix"