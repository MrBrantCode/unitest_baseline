"""
QUESTION:
Recently, Greg got a grid with n rows and m columns. Rows are indexed from 1 to n and columns are indexed from 1 to m. The cell $ ( i , j )$ is the cell of intersection of row i and column j. Each cell has a number written on it. The number written on cell  $( i , j )$  is equal to  $(i+j)$.  
Now, Greg wants to select some cells from the grid, such that for every pair of  selected cells ,the numbers on the cells are co-prime.  Determine the maximum number of cells that Greg can select.

------ Input  ------ 

Single line containing  integers n and m denoting number of rows and number of columns respectively.

------ Output ------ 

Single line containing the answer.

------ Constraints ------ 

$$1 ≤ n,m ≤ 10^{6}$$

----- Sample Input 1 ------ 
3 4

----- Sample Output 1 ------ 
4
"""

def max_coprime_cells(n, m):
    # Precompute the sieve of Eratosthenes up to n + m
    max_size = n + m + 1
    is_prime = [True] * max_size
    
    for i in range(2, max_size):
        if is_prime[i]:
            for j in range(2 * i, max_size, i):
                is_prime[j] = False
    
    # Calculate the cumulative count of primes up to each number
    prime_count = [0] * max_size
    count = 0
    for i in range(2, max_size):
        if is_prime[i]:
            count += 1
        prime_count[i] = count
    
    # The result is the number of primes up to n + m
    return prime_count[n + m]