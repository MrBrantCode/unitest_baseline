"""
QUESTION:
Implement a function `extended_euclidean(a, b)` to find the GCD (Greatest Common Divisor) of two positive integers `a` and `b` using the extended Euclidean algorithm. The function should also print out the intermediate steps of the algorithm and return the GCD along with the coefficients `x` and `y` such that `ax + by = GCD(a, b)`. The input `a` and `b` are positive integers.
"""

def extended_euclidean(a, b):
    # Initialize variables
    x, y, prev_x, prev_y = 0, 1, 1, 0
    step = 1
    
    # Perform the extended Euclidean algorithm
    while b != 0:
        prev_a = a
        q, r = divmod(a, b)
        a, b = b, r
        x, prev_x = prev_x - q * x, x
        y, prev_y = prev_y - q * y, y
        
        # Print intermediate step
        print("Step {}: {} = {} * {} + {}, x = {}, y = {}".format(step, prev_a, a, q, r, prev_x, prev_y))
        step += 1
    
    # Print final step
    print("GCD({}, {}) = {}, x = {}, y = {}".format(a, 0, a, prev_x, prev_y))
    
    return a, prev_x, prev_y