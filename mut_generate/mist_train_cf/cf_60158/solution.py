"""
QUESTION:
Write a recursive function called `recursive_count` that takes an integer `n` as input and prints the numbers from `n` to 15. The function should have a termination condition to prevent infinite recursion when the count reaches 16. Additionally, it should validate that the input is a numeric value.
"""

def recursive_count(n):    
    if not isinstance(n, int): 
        return 'Error: input must be an integer'
    if n > 15: 
        return
    print(n)
    recursive_count(n+1)