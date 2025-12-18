"""
QUESTION:
Create a function `sum_to_n` that calculates the sum of all integers from `n` down to 1 using a while loop. The loop should terminate when the sum exceeds 10,000 or when all integers down to 1 have been included. Implement a sophisticated loop termination command using the `break` statement.
"""

def sum_to_n(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
        if total > 10000:
            break
    return total