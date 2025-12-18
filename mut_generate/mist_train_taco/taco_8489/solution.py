"""
QUESTION:
You have a string A = A_1 A_2 ... A_n consisting of lowercase English letters.

You can choose any two indices i and j such that 1 \leq i \leq j \leq n and reverse substring A_i A_{i+1} ... A_j.

You can perform this operation at most once.

How many different strings can you obtain?

Constraints

* 1 \leq |A| \leq 200,000
* A consists of lowercase English letters.

Input

Input is given from Standard Input in the following format:


A


Output

Print the number of different strings you can obtain by reversing any substring in A at most once.

Examples

Input

aatt


Output

5


Input

xxxxxxxxxx


Output

1


Input

abracadabra


Output

44
"""

from collections import defaultdict

def count_distinct_reversed_strings(A: str) -> int:
    N = len(A)
    cnt = defaultdict(int)
    ans = 1 + N * (N - 1) // 2
    
    for a in A:
        ans -= cnt[a]
        cnt[a] += 1
    
    return ans