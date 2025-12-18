"""
QUESTION:
Given is a positive integer N.

Find the number of pairs (A, B) of positive integers not greater than N that satisfy the following condition:
 - When A and B are written in base ten without leading zeros, the last digit of A is equal to the first digit of B, and the first digit of A is equal to the last digit of B.

-----Constraints-----
 - 1 \leq N \leq 2 \times 10^5
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the answer.

-----Sample Input-----
25

-----Sample Output-----
17

The following 17 pairs satisfy the condition: (1,1), (1,11), (2,2), (2,22), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (11,1), (11,11), (12,21), (21,12), (22,2), and (22,22).
"""

def count_valid_pairs(N: int) -> int:
    # Initialize a 10x10 matrix to count pairs based on their first and last digits
    l = [[0] * 10 for _ in range(10)]
    
    # Populate the matrix with counts of numbers based on their first and last digits
    for i in range(1, N + 1):
        st = str(i)
        start = int(st[0])
        end = int(st[-1])
        l[start][end] += 1
    
    # Calculate the number of valid pairs
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += l[i][j] * l[j][i]
    
    return ans