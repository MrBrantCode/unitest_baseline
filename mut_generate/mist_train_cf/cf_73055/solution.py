"""
QUESTION:
Find a function named `find_quad` that takes two parameters: an integer `y` and a list of integers `z`, and returns the smallest Pythagorean quadruplet with a sum equal to `y`, using only unique integers from `z` and following the Pythagorean triplet rule where `a^2 + b^2 = c^2`.
"""

from itertools import combinations

def find_quad(y, z):
    quads = []
    # Get unique values from z
    z = list(set(z))
    # Find all possible combinations of 3 numbers (a,b,c) from z where a<b<c
    triples = [seq for seq in combinations(z, 3) if seq[0]<seq[1]<seq[2]]
    # Checking each combination
    for triple in triples:
        a, b, c = triple
        # If it is a Pythagorean Triple
        if a**2 + b**2 == c**2:
            # Find the fourth number
            for num in z:
                # Is not in the current triple and sums to y
                if num != a and num != b and num != c and a + b + c + num == y:
                    quads.append((a, b, c, num))
    # Return the smallest pythagorean quadruplet
    if quads:
        return min(quads, key=sum)
    else:
        return None