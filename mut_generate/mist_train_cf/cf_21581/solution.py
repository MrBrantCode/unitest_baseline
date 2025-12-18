"""
QUESTION:
Create a function `lucas(n)` that calculates the nth element of the Lucas sequence, where the sequence is defined by the recurrence relation: 
- The first two numbers in the sequence are 2 and 1.
- Each subsequent number in the sequence is the sum of the two preceding ones.
The function should be able to handle large values of n, up to 10^6.
"""

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        prev_prev = 2
        prev = 1
        for i in range(2, n + 1):
            curr = prev_prev + prev
            prev_prev = prev
            prev = curr
        return curr