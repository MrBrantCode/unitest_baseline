"""
QUESTION:
Create a function named `combinations` that takes two parameters: `string` (a given string of characters) and `n` (the number of characters in each combination). The function should return a lexicographically sorted array of strings, where each string is a unique combination of `n` characters from `string`.
"""

def combinations(string, n):
    # Base case: when n is 0, return an empty string
    if n == 0:
        return ['']
    
    # Base case: when string is empty or its length is less than n, return an empty list
    if not string or len(string) < n:
        return []
    
    # Recursive case: for each character in the string, find all combinations of n-1 characters from the remaining string
    result = []
    for i in range(len(string)):
        char = string[i]
        remaining = string[i+1:]
        combinations_of_remaining = combinations(remaining, n-1)
        
        # Append the character to each combination and add it to the result
        for combo in combinations_of_remaining:
            result.append(char + combo)
    
    # Sort the result lexicographically and return it
    return sorted(result)