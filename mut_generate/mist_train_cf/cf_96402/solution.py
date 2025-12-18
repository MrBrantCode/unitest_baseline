"""
QUESTION:
Write a function named `delete_chars(A, B)` that takes two strings `A` and `B` as input and returns a string after deleting all characters in `A` that also appear in `B` or appear more than once consecutively.
"""

def delete_chars(A, B):
    # Convert A and B into lists to make modifications easier
    A = list(A)
    B = list(B)
    
    # Initialize a pointer to keep track of the current position in A
    i = 0
    
    # Iterate through each character in A
    while i < len(A):
        # Check if the character is in B or if it appears more than once consecutively
        if A[i] in B or (i > 0 and A[i] == A[i-1]):
            # Delete the character from A
            del A[i]
        else:
            # Move to the next character in A
            i += 1
    
    # Convert A back into a string and return it
    return ''.join(A)