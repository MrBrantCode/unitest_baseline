"""
QUESTION:
Develop a function named `hugeSum` that calculates the final value of a variable `a` that is incremented by all integers from 0 to a given number `high`. The function should prevent integer overflow by dividing the calculation into smaller sums. The function should take two parameters: `high` (the upper limit of the range) and `step` (the size of each range to prevent overflow).
"""

def hugeSum(high, step):
    a = 0
    low = 0

    while high > 0:
        top = min(high, low + step - 1)
        a += (top * (top + 1) // 2) - ((low - 1) * low // 2)
        low += step
        high -= step
    
    return a