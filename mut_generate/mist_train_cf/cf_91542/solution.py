"""
QUESTION:
Create a function `generate_pythagorean_triples(limit)` that generates all Pythagorean triples with sides `a`, `b`, and `c` where `a`, `b`, and `c` are integers, `a <= b`, and the sum of `a`, `b`, and `c` is less than or equal to 50. The function should return a list of all such triples where `a` and `b` are less than or equal to the given `limit`.
"""

def generate_pythagorean_triples(limit):
    triples = []
    for a in range(1, limit+1):
        for b in range(a, limit+1):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and a + b + c <= 50:
                triples.append((a, b, int(c)))
    return triples