"""
QUESTION:
Write a function named `get_distinct_permutations` that takes a string as input and returns all distinct permutations of the string. The function should be able to handle strings with duplicate characters and should not use any built-in library functions or modules that directly solve this problem.
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