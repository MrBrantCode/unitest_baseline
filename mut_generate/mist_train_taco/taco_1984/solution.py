"""
QUESTION:
Its Diwali time and little Roy thought of an interesting design for Rangoli.
He created an N x N grid. Roy fills some of the cells of grid with red color.

Cell located at ith row and jth column is colored if i+j is prime. Consider Zero-based numbering of grid. (See Sample Test Case Explanation for clarification)

Roy wants to know how many cells he will have to color given the size of grid N.

Input:

One integer indicating size of grid N

Output:

Print a single integer, number of cells Roy will have to color. Since answer can be very large output it modulo 1000000007

Constraints:

1 ≤ N ≤1000000

Sample Test Case Explanation:SAMPLE INPUT
3

SAMPLE OUTPUT
5

Explanation

As shown in the image above, five cells (0,2), (1,1), (1,2), (2,0), (2,1) are colored red because for (i,j) i+j for these cells results into a prime number.
"""

def count_colored_cells(N):
    def sieve(n):
        is_prime = [True] * (n+1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, n+1):
            if is_prime[i]:
                for j in range(i+i, n+1, i):
                    is_prime[j] = False
        return is_prime

    MOD = 1000000007
    is_prime = sieve(N + N)
    total = 0
    
    for i in range(N):
        if is_prime[i]:
            total += i + 1
    
    nn1 = N + N - 1
    for i in range(N, nn1):
        if is_prime[i]:
            total += nn1 - i
    
    return total % MOD