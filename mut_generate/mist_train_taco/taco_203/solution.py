"""
QUESTION:
In 2937, DISCO creates a new universe called DISCOSMOS to celebrate its 1000-th anniversary.

DISCOSMOS can be described as an H \times W grid. Let (i, j) (1 \leq i \leq H, 1 \leq j \leq W) denote the square at the i-th row from the top and the j-th column from the left.

At time 0, one robot will be placed onto each square. Each robot is one of the following three types:

* Type-H: Does not move at all.
* Type-R: If a robot of this type is in (i, j) at time t, it will be in (i, j+1) at time t+1. If it is in (i, W) at time t, however, it will be instead in (i, 1) at time t+1. (The robots do not collide with each other.)
* Type-D: If a robot of this type is in (i, j) at time t, it will be in (i+1, j) at time t+1. If it is in (H, j) at time t, however, it will be instead in (1, j) at time t+1.



There are 3^{H \times W} possible ways to place these robots. In how many of them will every square be occupied by one robot at times 0, T, 2T, 3T, 4T, and all subsequent multiples of T?

Since the count can be enormous, compute it modulo (10^9 + 7).

Constraints

* 1 \leq H \leq 10^9
* 1 \leq W \leq 10^9
* 1 \leq T \leq 10^9
* H, W, T are all integers.

Input

Input is given from Standard Input in the following format:


H W T


Output

Print the number of ways to place the robots that satisfy the condition, modulo (10^9 + 7).

Examples

Input

2 2 1


Output

9


Input

869 120 1001


Output

672919729
"""

def gcd(x, y):
    if x < y:
        (x, y) = (y, x)
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def count_valid_robot_placements(H, W, T):
    mod = 10 ** 9 + 7
    
    # Calculate the greatest common divisor (GCD) of H and T
    h = gcd(H, T)
    
    # Calculate the greatest common divisor (GCD) of W and T
    w = gcd(W, T)
    
    # Reduce H and W by their respective GCDs
    H //= h
    W //= w
    
    # Calculate the number of valid placements
    ans = pow(2, H, mod) + pow(2, W, mod) + pow(2, gcd(H, W), mod) - 3
    
    # Return the result modulo (10^9 + 7)
    return pow(ans, h * w, mod)