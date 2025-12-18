"""
QUESTION:
Imagine that you are given two sticks. You want to end up with three sticks of equal length. You are allowed to cut either or both of the sticks to accomplish this, and can throw away leftover pieces.

Write a function, maxlen, that takes the lengths of the two sticks (L1 and L2, both positive values), that will return the maximum length you can make the three sticks.
"""

def maxlen(L1, L2):
    # Sort the lengths to identify the smaller and larger stick
    sm, lg = sorted((L1, L2))
    
    # Calculate the maximum possible length for the three sticks
    # This is the minimum of the following:
    # 1. The maximum length if we cut the larger stick into three parts
    # 2. The length of the smaller stick (since we can't make all three sticks longer than the smaller stick)
    # 3. The maximum length if we cut the larger stick into two parts and use the smaller stick as the third part
    return min(max(lg / 3, sm), lg / 2)