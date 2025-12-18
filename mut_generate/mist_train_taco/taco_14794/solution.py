"""
QUESTION:
Find the smallest possible sum of the digits in the decimal notation of a positive multiple of K.

-----Constraints-----
 - 2 \leq K \leq 10^5
 - K is an integer.

-----Input-----
Input is given from Standard Input in the following format:
K

-----Output-----
Print the smallest possible sum of the digits in the decimal notation of a positive multiple of K.

-----Sample Input-----
6

-----Sample Output-----
3

12=6×2 yields the smallest sum.
"""

import collections

def smallest_sum_of_digits_of_multiple(K: int) -> int:
    lst = [K + 1] * K
    q = collections.deque([1])
    lst[1] = 1
    
    while q:
        a = q.pop()
        if lst[a * 10 % K] > lst[a]:
            lst[a * 10 % K] = lst[a]
            q.append(a * 10 % K)
        if lst[(a + 1) % K] >= lst[a] + 1:
            lst[(a + 1) % K] = lst[a] + 1
            q.appendleft((a + 1) % K)
    
    return lst[0]