"""
QUESTION:
Write a function `find_longest_substring(string, k)` that finds the longest substring that appears at least `k` times in the given `string`. The function should have a time complexity of O(n), where n is the length of the input string. If the input string is empty or contains fewer than `k` occurrences of any substring, the function should return `None`. In cases where multiple substrings have the same maximum length, the function should return the first occurrence of the longest substring.
"""

def find_longest_substring(string, k):
    if len(string) == 0:
        return None
    
    if k <= 0:
        return None
    
    substring_count = {}
    max_length = 0
    max_substring = ""
    
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            
            if substring not in substring_count:
                substring_count[substring] = 1
            else:
                substring_count[substring] += 1
            
            if substring_count[substring] >= k and len(substring) > max_length:
                max_length = len(substring)
                max_substring = substring
    
    if max_length == 0:
        return None
    
    return max_substring