"""
QUESTION:
A positive integer X is said to be a lunlun number if and only if the following condition is satisfied:
 - In the base ten representation of X (without leading zeros), for every pair of two adjacent digits, the absolute difference of those digits is at most 1.
For example, 1234, 1, and 334 are lunlun numbers, while none of 31415, 119, or 13579 is.
You are given a positive integer K. Find the K-th smallest lunlun number.

-----Constraints-----
 - 1 \leq K \leq 10^5
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
K

-----Output-----
Print the answer.

-----Sample Input-----
15

-----Sample Output-----
23

We will list the 15 smallest lunlun numbers in ascending order:
1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
21,
22,
23.

Thus, the answer is 23.
"""

from collections import deque

def find_kth_lunlun_number(K: int) -> int:
    que = deque([i for i in range(1, 10, 1)])
    
    for _ in range(K):
        x = que.popleft()
        if x % 10 == 0:
            que.append(x * 10)
            que.append(x * 10 + 1)
        elif x % 10 == 9:
            que.append(x * 10 + 8)
            que.append(x * 10 + 9)
        else:
            que.append(x * 10 + x % 10 - 1)
            que.append(x * 10 + x % 10)
            que.append(x * 10 + x % 10 + 1)
    
    return x