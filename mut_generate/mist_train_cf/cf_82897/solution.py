"""
QUESTION:
Create a function `evaluate(p, q)` that takes two odd integers `p` and `q` as input and returns `True` if the mathematical statement `((p*q) + (p-q) ** 2) // 2` equals a specific value for `p = 7` and `q = 15`.
"""

def evaluate(p, q):
    return ((p*q) + (p-q) ** 2) // 2 == 27