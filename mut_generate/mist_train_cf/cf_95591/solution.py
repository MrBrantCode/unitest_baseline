"""
QUESTION:
Create a function named `concatenate_unique_sorted` that takes two strings `s1` and `s2` as inputs. The function should return a string that is the concatenation of `s1` and `s2`, with all duplicate characters removed and the remaining characters sorted in ascending order. The function should have a time complexity of O(nlogn) and a space complexity of O(n), where n is the total number of unique characters in both input strings.
"""

def concatenate_unique_sorted(s1, s2):
    concatenated = s1 + s2
    unique_chars = set()
    
    for char in concatenated:
        if char not in unique_chars:
            unique_chars.add(char)
    
    sorted_chars = sorted(unique_chars)
    result = ''.join(sorted_chars)
    
    return result