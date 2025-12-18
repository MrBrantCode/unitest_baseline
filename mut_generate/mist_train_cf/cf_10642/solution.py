"""
QUESTION:
Construct a context-free grammar (CFG) for the language {anbmcn | n, m ≥ 0} with the following conditions: 
- Each 'a' is followed by 'b' and then 'c'.
- The number of 'a's is equal to the number of 'b's which is equal to the number of 'c's. 
- The number of 'a's is greater than or equal to the number of 'b's.
- The number of 'b's is greater than or equal to the number of 'c's.
"""

def entrance(n, m):
    return "a" * n + "b" * n + "c" * m