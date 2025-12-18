"""
QUESTION:
Create a function `get_distinct_permutations(string)` that returns all distinct permutations of the input string, where a distinct permutation is defined as a permutation that is unique among all permutations of the string. The function should handle cases where the string may contain duplicate characters and should not use any built-in library functions or modules that directly solve this problem.
"""

def get_distinct_permutations(string):
    if len(string) == 1:
        return [string]
    
    distinct_permutations = []
    used_chars = set()
    
    for i in range(len(string)):
        if string[i] in used_chars:
            continue
        
        used_chars.add(string[i])
        sub_permutations = get_distinct_permutations(string[:i] + string[i+1:])
        
        for sub_permutation in sub_permutations:
            distinct_permutations.append(string[i] + sub_permutation)
    
    return distinct_permutations