"""
QUESTION:
Create a function `calculate_similarity` that takes two string inputs `A` and `B` where `A` is a shorter string and `B` is a more detailed description of `A`. The function should return a percentage match between the two strings based on the following rules:
- If all values of `A` are found in `B`, return 100%.
- If similar values of `A` are found in `B`, return 80%.
- If no values of `A` are found in `B`, return 0%.
Note: The function should be case-insensitive and should not require any external parameters or dataframes.
"""

def calculate_similarity(A, B):
    A = A.lower()
    B = B.lower()
    
    # check if all values of A are found in B
    if all(char in B for char in A):
        return 100
    
    # check if similar values of A are found in B
    elif any(char in B for char in A):
        return 80
    
    # if no values of A are found in B
    else:
        return 0