"""
QUESTION:
The problem statement is simple. You are given a string and you are 
supposed to print all the distinct permutations of the string, as they would appear in an dictionary. 

INPUT
The first and only line of the input contains a single string, S.

OUTPUT
The output contains the required strings, each string in a seperate line.

CONSTRAINTS
1 ≤ |S| ≤ 9

SAMPLE INPUT
abc

SAMPLE OUTPUT
abc
acb
bac
bca
cab
cba
"""

from itertools import permutations

def generate_distinct_permutations(s: str) -> list[str]:
    # Generate all permutations of the string
    perms = [''.join(p) for p in permutations(s)]
    
    # Convert to a set to remove duplicates and back to a list
    perms = list(set(perms))
    
    # Sort the permutations in dictionary order
    perms.sort()
    
    return perms