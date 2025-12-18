"""
QUESTION:
Write a function that evaluates the bitwise AND of A, B, and C with specific values. The function should take three integer parameters A, B, and C, and use bitwise AND to check if A has 1, B has 2, and C has 3 as their respective least significant bits. The function should return True if all conditions are met, and False otherwise.
"""

def entrance(A, B, C):
    return (A & 1) and (B & 2) and (C & 3)