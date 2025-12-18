"""
QUESTION:
Snuke has an integer sequence A of length N.

He will make three cuts in A and divide it into four (non-empty) contiguous subsequences B, C, D and E. The positions of the cuts can be freely chosen.

Let P,Q,R,S be the sums of the elements in B,C,D,E, respectively. Snuke is happier when the absolute difference of the maximum and the minimum among P,Q,R,S is smaller. Find the minimum possible absolute difference of the maximum and the minimum among P,Q,R,S.

Constraints

* 4 \leq N \leq 2 \times 10^5
* 1 \leq A_i \leq 10^9
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 ... A_N


Output

Find the minimum possible absolute difference of the maximum and the minimum among P,Q,R,S.

Examples

Input

5
3 2 4 1 2


Output

2


Input

10
10 71 84 33 6 47 23 25 52 64


Output

36


Input

7
1 2 3 1000000000 4 5 6


Output

999999994
"""

def find_min_abs_difference(N, A):
    from itertools import accumulate
    
    # Calculate the prefix sums
    C = [0] + list(accumulate(A))
    
    # Initialize pointers and the result variable
    l, r = 1, 3
    x = 10 ** 16
    
    # Iterate over possible middle cut positions
    for m in range(2, N - 1):
        # Initialize sums for the four subsequences
        a, b, c, d = C[l], C[m] - C[l], C[r] - C[m], C[N] - C[r]
        
        # Adjust the left cut position
        while l < m - 1 and abs(C[m] - C[l + 1] * 2) < abs(a - b):
            l += 1
            a, b = C[l], C[m] - C[l]
        
        # Adjust the right cut position
        while r < N - 1 and abs(C[N] - C[r + 1] * 2 + C[m]) < abs(c - d):
            r += 1
            c, d = C[r] - C[m], C[N] - C[r]
        
        # Update the minimum absolute difference
        x = min(x, max(a, b, c, d) - min(a, b, c, d))
    
    return x