"""
QUESTION:
Given is a number sequence A of length N.
Find the number of integers i \left(1 \leq i \leq N\right) with the following property:
 - For every integer j \left(1 \leq j \leq N\right) such that i \neq j , A_j does not divide A_i.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq N \leq 2 \times 10^5
 - 1 \leq A_i \leq 10^6

-----Input-----
Input is given from Standard Input in the following format:
N
A_1 A_2 \cdots A_N

-----Output-----
Print the answer.

-----Sample Input-----
5
24 11 8 3 16

-----Sample Output-----
3

The integers with the property are 2, 3, and 4.
"""

def count_non_divisible_elements(N, A):
    A.sort()
    d = {}
    for x in A:
        d[x] = d.get(x, 0) + 1
    
    ans = 0
    ok = [1] * (10 ** 6 + 1)
    
    for x in list(d.keys()):
        if ok[x]:
            for j in range(2, 10 ** 6 // x + 1):
                ok[j * x] = 0
            if d[x] == 1:
                ans += 1
    
    return ans