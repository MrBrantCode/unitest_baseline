"""
QUESTION:
Create a function `compare_values` that takes two arguments, A and B, and checks if A is greater than B. The function should only accept positive integers within the range of 1 to 1000 for both A and B. If the conditions are met and A is greater than B, the function should return "A is greater than B".
"""

def compare_values(A, B):
    if 0 < A <= 1000 and 0 < B <= 1000:
        if A > B:
            return "A is greater than B"
    return None