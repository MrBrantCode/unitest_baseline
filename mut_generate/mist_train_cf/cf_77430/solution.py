"""
QUESTION:
Write a function `prime_composite_numbers` that takes an array of integers as input and returns a tuple (x, y, z, w). Here, 'x' should be the smallest positive prime number, 'y' should be the largest negative prime number, 'z' should be the smallest positive composite number, and 'w' should be the largest negative composite number in the array. If a number doesn't meet the criteria, return None. Assume prime and composite numbers can be both positive and negative.
"""

def prime_composite_numbers(arr):
    x, y, z, w = None, None, None, None

    for i in arr:
        # check for primes
        if (i == 2 or i == -2) or (i % 2 != 0 and i != 1 and i != -1 and all(i % j != 0 for j in range(3, int(abs(i) ** 0.5) + 1, 2))):
            if i > 0 and (x is None or i < x):
                x = i
            elif i < 0 and (y is None or i > y):
                y = i
                
        # check for composites
        elif abs(i) >= 2 and (i % 2 == 0 and i != 2 and i != -2 or any(i % j == 0 for j in range(3, int(abs(i) ** 0.5) + 1, 2))):
            if i > 0 and (z is None or i < z):
                z = i
            elif i < 0 and (w is None or i > w):
                w = i

    return (x, y, z, w)