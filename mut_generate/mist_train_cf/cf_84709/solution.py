"""
QUESTION:
Create a function `solve_puzzle` that generates all possible unique rearrangements of the string "ABC123" where each rearrangement starts with a letter, does not end with the same character it begins with, and contains at least one valid integer arithmetic operation as a substring. The arithmetic operation can be in the middle of two characters and does not include the use of arithmetic operators from the original string.
"""

import itertools

# possible arithmetic operations
arith_ops = ['+', '-', '*', '/']

# Check if the substring forms a valid arithmetic operation
def check_arith(sub):
    for op in arith_ops:
        if op in sub:
            try:
                # Does it calculate to an integer?
                if eval(sub) == int(eval(sub)):
                    return True
            except ZeroDivisionError:
                return False
    return False

# Function to solve the puzzle
def solve_puzzle():
    # First we get all permutations of ABC123 starting with a letter
    permutations = [''.join(p) for p in itertools.permutations("ABC123")
                    if p[0].isalpha() and p[0] != p[-1]]
    
    # Filtering out permutations satisfying arithmetic operation constraint
    final_permutations = []
    
    for permutation in permutations:
        for i in range(1, len(permutation)):
            for j in range(i+2, len(permutation)+1):
                if check_arith(permutation[i:j]):
                    final_permutations.append(permutation)
                    break
    
    return final_permutations