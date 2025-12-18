"""
QUESTION:
Write a function `gcd(n1, n2)` that calculates the greatest common divisor (GCD) of two numbers `n1` and `n2` using the Euclidean algorithm. The function should have a time complexity of O(log(min(n1, n2))) and a space complexity of O(1).
"""

def gcd(n1, n2):
    # Euclidean algorithm
    while n2 != 0:
        temp = n2
        n2 = n1 % n2
        n1 = temp
    
    return n1