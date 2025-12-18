"""
QUESTION:
Develop a function `longest_common_prefix(strings)` that takes a list of strings as input and returns the longest common prefix among all the strings in the list, considering case sensitivity. The function should handle any character encoding, including Unicode. The list of strings can contain up to 10^6 strings, and the maximum length of each string is 10^4 characters. The time complexity of the function should be O(N*M), where N is the length of the list of strings and M is the average length of the strings. The function should use O(M) extra space, where M is the maximum length of the strings.
"""

def longest_common_prefix(strings):
    if not strings:
        return ""
    
    shortest_str = min(strings, key=len)
    
    for i, char in enumerate(shortest_str):
        for other in strings:
            if other[i] != char:
                return shortest_str[:i]
    
    return shortest_str