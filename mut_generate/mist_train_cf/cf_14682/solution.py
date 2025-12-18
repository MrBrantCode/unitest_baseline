"""
QUESTION:
Write a function named `gcd` that takes two integers as input and returns their greatest common divisor using the Euclidean Algorithm. The function should have a time complexity of O(log(min(a,b))) and a space complexity of O(1), where a and b are the input integers.
"""

def gcd(a, b):
    # Step 2
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Step 3
    while b != 0:
        # Step 3a
        r = a % b
        
        # Step 3b
        a = b
        b = r
    
    # Step 4
    return a