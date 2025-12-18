"""
QUESTION:
Create a function named cycpattern_check that takes two string parameters, a and b. The function should check if string b or any of its cyclic permutations is a contiguous subsequence within string a. The function should be case-insensitive and ignore non-alphanumeric characters.
"""

def cycpattern_check(a, b):
    def clean(s):
        return ''.join([c for c in s.lower() if c.isalnum()])
    
    a = clean(a)
    b = clean(b)
    
    def cyclic_permutations(s):
        return [s[i:] + s[:i] for i in range(len(s))]
    
    cyclic_permutations_b = cyclic_permutations(b)
    
    for permutation in cyclic_permutations_b:
        if permutation in a:
            return True
    return False