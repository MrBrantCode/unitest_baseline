"""
QUESTION:
Write a function `longest_common_substring(json1, json2)` that finds the longest common substring between two JSON data sets using dynamic programming. The function should take two JSON strings as input and return the longest common substring. The function should handle large JSON data sets containing multiple attributes.
"""

import json
def longest_common_substring(json1, json2):
    dict1 = json.loads(json1)
    dict2 = json.loads(json2)
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    table = [[0 for _ in range(len(keys2) + 1)] for _ in range(len(keys1) + 1)]
    longest_substring = ""
    longest_substring_end = 0
    for i in range(1, len(keys1) + 1):
        for j in range(1, len(keys2) + 1):
            if keys1[i-1] == keys2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
                if table[i][j] > len(longest_substring):
                    longest_substring = keys1[i-table[i][j]:i]
                    longest_substring_end = i
            else:
                table[i][j] = 0
    return longest_substring