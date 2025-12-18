"""
QUESTION:
Create a function `lucas_sequence(n)` that returns the nth number in the Lucas sequence, where the sequence starts with 2 and 1, and each subsequent number is the sum of the previous two.
"""

def lucas_sequence(n):
    lucas = [2, 1]
    for i in range(2, n):
        lucas.append(lucas[i-1] + lucas[i-2])
    return lucas[n-1]