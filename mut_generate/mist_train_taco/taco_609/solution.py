"""
QUESTION:
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.


For example, with A = "abcd" and B = "cdabcdab". 


Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").


Note:
The length of A and B will be between 1 and 10000.
"""

def repeated_string_match(A: str, B: str) -> int:
    if not set(B).issubset(set(A)):
        return -1
    
    max_rep = len(B) // len(A) + 3
    A_new = A
    
    for i in range(1, max_rep):
        if B in A_new:
            return i
        A_new += A
    
    return -1