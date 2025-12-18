"""
QUESTION:
Write a function `delete_common_chars(A, B)` that takes two strings `A` and `B` as input and returns a string where all characters in `A` that appear in `B` (case-insensitive) and any consecutively repeated characters in `A` (case-insensitive) are deleted.
"""

def delete_common_chars(A, B):
    # Remove characters in B from A
    A = ''.join(char for char in A if char.lower() not in B.lower())
    
    # Remove consecutively repeated characters
    modified_A = ''
    for i in range(len(A)):
        if i == 0 or A[i] != A[i-1]:
            modified_A += A[i]
    
    return modified_A