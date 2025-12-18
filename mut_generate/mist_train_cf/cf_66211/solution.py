"""
QUESTION:
Write a function `alpha_finder(sequence, alpha, num)` that takes a string `sequence`, a character `alpha`, and an integer `num` as inputs. The function should return `True` if `alpha` appears exactly `num` times in `sequence`, ignoring case. If `num` is 0, the function should return `True` if `alpha` does not appear in `sequence`. The function should handle both lowercase and uppercase characters equally.
"""

def alpha_finder(sequence, alpha, num):
    sequence = sequence.lower()
    alpha = alpha.lower()
    count = sequence.count(alpha)
    
    return (num == 0 and count == 0) or count == num