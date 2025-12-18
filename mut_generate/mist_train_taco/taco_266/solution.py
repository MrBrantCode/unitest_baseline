"""
QUESTION:
Given are a sequence of N positive integers A_1, A_2, \ldots, A_N, and a positive integer K.
Find the number of non-empty contiguous subsequences in A such that the remainder when dividing the sum of its elements by K is equal to the number of its elements. We consider two subsequences different if they are taken from different positions, even if they are equal sequences.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq N \leq 2\times 10^5
 - 1 \leq K \leq 10^9
 - 1 \leq A_i \leq 10^9

-----Input-----
Input is given from Standard Input in the following format:
N K
A_1 A_2 \cdots A_N

-----Output-----
Print the number of subsequences that satisfy the condition.

-----Sample Input-----
5 4
1 4 2 3 5

-----Sample Output-----
4

Four sequences satisfy the condition: (1), (4,2), (1,4,2), and (5).
"""

from collections import defaultdict
from itertools import accumulate

def count_valid_subsequences(N, K, A):
    a = list(accumulate([0] + A))
    a = [(a[i] - i) % K for i in range(N + 1)]
    answer = 0
    dic = defaultdict(int)
    for i, x in enumerate(a):
        answer += dic[x]
        dic[x] += 1
        if i >= K - 1:
            dic[a[i - K + 1]] -= 1
    return answer