"""
QUESTION:
Write a function `find_gcf(a, b, c)` that takes three integers `a`, `b`, and `c` as input and returns their greatest common factor. The time complexity of the function should be O(n log n), where n is the largest number among the three.
"""

def find_gcf(a, b, c):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    gcf_ab = gcd(a, b)
    gcf_abc = gcd(gcf_ab, c)
    return gcf_abc