"""
QUESTION:
Write a function named `longest_common_suffix` that finds the longest common suffix among a given set of strings. The function should handle cases where strings contain special characters or numbers and efficiently perform for large data sets.
"""

def longest_common_suffix(strs):
    if not strs:
        return ""
        
    shortest_str = min(strs, key=len)
    
    for i in range(len(shortest_str)):
        for other_str in strs:
            if other_str[::-1][i] != shortest_str[::-1][i]:
                return shortest_str[::-1][len(shortest_str)-i:]
    
    return shortest_str