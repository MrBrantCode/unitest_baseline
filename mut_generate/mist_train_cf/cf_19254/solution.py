"""
QUESTION:
Create a function named `concatenate_unique_sorted` that takes two strings `s1` and `s2` as inputs. The function should return a string that is the concatenation of `s1` and `s2` but with no duplicate characters, and the characters in the resulting string should be sorted in ascending order. The time complexity of the function should be O(nlogn) and the space complexity should be O(n), where n is the total number of characters in both input strings.
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