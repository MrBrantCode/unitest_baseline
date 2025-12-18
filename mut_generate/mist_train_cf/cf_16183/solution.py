"""
QUESTION:
Write a function `longest_common_prefix` that takes an array of strings as input and returns the longest common prefix string that is at least 5 characters long. The input array can contain up to 200 strings, each with a maximum length of 100 characters, and may include uppercase and lowercase letters, numbers, and special characters. The time complexity of the solution should be O(n*m), where n is the length of the input array and m is the maximum length of the strings.
"""

def longest_common_prefix(strings):
    commonPrefix = ""
    
    if len(strings) == 0:
        return commonPrefix
    
    for i in range(len(strings[0])):
        for j in range(1, len(strings)):
            if i >= len(strings[j]) or strings[j][i] != strings[0][i]:
                return commonPrefix
            
        commonPrefix += strings[0][i]
    
    if len(commonPrefix) < 5:
        return ""
    
    return commonPrefix