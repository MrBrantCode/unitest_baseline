"""
QUESTION:
Write a function named `longest_common_substring` that takes two JSON strings as input. The function should find the longest common substring between the keys of the two JSON objects. The function should use a dynamic programming approach and state the time and space complexity of the algorithm used to solve this problem. The function should return the longest common substring. Assume that the input JSON strings are valid and contain multiple attributes.
"""

import json

def longest_common_substring(json1, json2):
    # Convert JSON strings to dictionaries
    dict1 = json.loads(json1)
    dict2 = json.loads(json2)
    
    # Get keys from both dictionaries
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    
    # Initialize dynamic programming table
    table = [[0 for _ in range(len(keys2) + 1)] for _ in range(len(keys1) + 1)]
    
    # Initialize variables to keep track of longest substring and its ending index
    longest_substring = ""
    longest_substring_end = 0
    
    # Fill dynamic programming table
    for i in range(1, len(keys1) + 1):
        for j in range(1, len(keys2) + 1):
            if keys1[i-1] == keys2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
                if table[i][j] > len(longest_substring):
                    longest_substring = keys1[i-table[i][j]:i]
                    longest_substring_end = i
            else:
                table[i][j] = 0
    
    # Return longest common substring
    return longest_substring