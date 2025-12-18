"""
QUESTION:
Compute the sum of two integers "a" and "b" with the given constraints: 
- Both integers are separated by a space.
- The integers can be extremely large, up to 10^18.
- The integers can be either positive or negative.
- The solution should have a time complexity of O(1).
"""

def add_strings(a, b):
    # Split the string into two numbers and convert them to integers
    a, b = int(a), int(b)
    
    # Calculate the sum
    sum = a + b
    
    # Return the sum
    return sum