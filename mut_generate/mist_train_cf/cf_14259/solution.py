"""
QUESTION:
Write a function `generate_strings(n)` that generates all possible strings of length n using characters A, B, and C, with at least one occurrence of each character.
"""

def generate_strings(n):
    # Base case
    if n == 3:
        return ['ABC']
    
    # Generate strings recursively
    sub_strings = generate_strings(n-1)
    strings = set()
    
    for sub_string in sub_strings:
        # Generate all possible strings by filling the remaining positions
        for char in ['A', 'B', 'C']:
            for i in range(len(sub_string)+1):
                new_string = sub_string[:i] + char + sub_string[i:]
                strings.add(new_string)
    
    return [s for s in strings if all(c in s for c in 'ABC')]