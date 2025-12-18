"""
QUESTION:
Implement the `find_substring` function, which returns the first index of the `substring` in the `string` if found, or -1 otherwise. The function should have a time complexity of O(n) and space complexity of O(1), where n is the length of the `string`.
"""

def find_substring(string, substring):
    n = len(string)
    m = len(substring)
    
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if string[i + j] != substring[j]:
                break
            j += 1
        if j == m:
            return i
    
    return -1  # If substring is not found