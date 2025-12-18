"""
QUESTION:
Create a function `amplify_complexity(m)` that takes a list `m` as input and returns a new list `m'`. In `m'`, values at indices that are not multiples of 5 remain the same as in `m`, while values at indices that are multiples of 5 are replaced with the same elements from `m` in sorted order.
"""

def amplify_complexity(m):
    # Extract elements at indices that are multiples of 5
    multiples_5 = [m[i] for i in range(len(m)) if i % 5 == 0]
    
    # Sort the multiples_5 list
    multiples_5.sort()

    # Create the m' list
    m_prime = [multiples_5.pop(0) if i%5==0 else m[i] for i in range(len(m))]

    return m_prime