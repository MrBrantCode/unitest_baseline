"""
QUESTION:
Write a function `delete_common_chars(A, B)` that takes two strings `A` and `B` as input. The function should delete characters in `A` that also appear in `B`, ignoring case sensitivity. Additionally, it should remove any characters in `A` that appear more than once consecutively, also ignoring case sensitivity. Return the modified string `A`.
"""

def delete_common_chars(A, B):
    # Remove characters in B from A
    A = ''.join(char for char in A if char.lower() not in B.lower())
    
    # Remove consecutively repeated characters
    modified_A = ''
    for i in range(len(A)):
        if i == 0 or A[i].lower() != A[i-1].lower():
            modified_A += A[i]
    
    return modified_A