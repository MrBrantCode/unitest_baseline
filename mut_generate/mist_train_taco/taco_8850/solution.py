"""
QUESTION:
We have N balls. The i-th ball has an integer A_i written on it.

For each k=1, 2, ..., N, solve the following problem and print the answer.  
 - Find the number of ways to choose two distinct balls (disregarding order) from the N-1 balls other than the k-th ball so that the integers written on them are equal.

-----Constraints-----
 - 3 \leq N \leq 2 \times 10^5
 - 1 \leq A_i \leq N
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
A_1 A_2 ... A_N

-----Output-----
For each k=1,2,...,N, print a line containing the answer.

-----Sample Input-----
5
1 1 2 1 2

-----Sample Output-----
2
2
3
2
3

Consider the case k=1 for example. The numbers written on the remaining balls are 1,2,1,2.

From these balls, there are two ways to choose two distinct balls so that the integers written on them are equal.

Thus, the answer for k=1 is 2.
"""

import collections

def count_equal_pairs_excluding_k(N, A):
    # Count the occurrences of each number
    c = collections.Counter(A)
    
    # Calculate the total number of pairs in the entire list
    total_pairs = sum((i * (i - 1) // 2 for i in c.values()))
    
    # Calculate the result for each k
    result = []
    for i in range(N):
        # Number of pairs excluding the i-th ball
        pairs_excluding_k = total_pairs - (c[A[i]] - 1)
        result.append(pairs_excluding_k)
    
    return result