"""
QUESTION:
Create a function named `generate_pythagorean_triples` that takes an integer `limit` as input. The function should generate and return all Pythagorean triples (a, b, c) where a and b are less than or equal to the given limit and a + b + c is less than or equal to 50. The function should return a list of tuples, where each tuple represents a Pythagorean triple.
"""

def generate_pythagorean_triples(limit):
    triples = []
    for a in range(1, limit+1):
        for b in range(a, limit+1):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and a + b + c <= 50:
                triples.append((a, b, int(c)))
    return triples