"""
QUESTION:
Create a function named `search_patterns` that takes two parameters: `s` (the string to be searched) and `patterns` (a list of strings representing the patterns to be found). The function should return a dictionary where each key is a pattern from the `patterns` list and each corresponding value is a list of indices where the pattern occurs in the string `s`. The function should be efficient enough to handle large strings.
"""

def search_patterns(s, patterns):
    results = {pattern: [] for pattern in patterns}
    for pattern in patterns:
        start = 0
        while start < len(s):
            start = s.find(pattern, start)
            if start == -1: 
                break
            else:
                results[pattern].append(start)
                start += 1
    return results