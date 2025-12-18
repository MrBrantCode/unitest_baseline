"""
QUESTION:
A plot of land can be described by $M x N$ dots such that horizontal and vertical distance between any two dots is 10m.
Mr. Wolf would like to build a house in the land such that all four sides of the house are equal. Help Mr. Wolf to find the total number of unique positions where houses can be built. Two positions are different if and only if their sets of four dots are different.

-----Input:-----
The first line of the input gives the number of test cases, $T$. $T$ lines follow. Each line has two integers $M$ and $N$: the number of dots in each row and column of the plot, respectively.

-----Output:-----
For each test case, output one single integer containing the total number of different positions where the house can be built.

-----Constraints-----
- $1 \leq T \leq 100$
- $2 \leq M \leq 10^9$
- $2 \leq N \leq 10^9$

-----Sample Input:-----
4

2 4

3 4

4 4

1000 500  

-----Sample Output:-----
3

10

20

624937395  

-----EXPLANATION:-----
Map 1

Map 2

Map 3
"""

def calculate_unique_house_positions(M, N):
    """
    Calculate the total number of unique positions where houses can be built on a plot of land described by M x N dots.

    Parameters:
    M (int): The number of dots in each row of the plot.
    N (int): The number of dots in each column of the plot.

    Returns:
    int: The total number of unique positions where houses can be built.
    """
    mod = 1000000007
    
    # Ensure M is the larger dimension
    if M < N:
        M, N = N, M
    
    y = N - 1
    
    # Calculate intermediate sums
    s1 = y * (y + 1) // 2 % mod
    s2 = y * (y + 1) * (2 * y + 1) // 6 % mod
    s3 = y * y * (y + 1) * (y + 1) // 4 % mod
    
    # Calculate the final answer
    ans = (M * N * s1 - (M + N) * s2 + s3) % mod
    
    return ans