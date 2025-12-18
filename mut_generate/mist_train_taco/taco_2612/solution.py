"""
QUESTION:
You are given an integer N. Among the divisors of N! (= 1 \times 2 \times ... \times N), how many Shichi-Go numbers (literally "Seven-Five numbers") are there?
Here, a Shichi-Go number is a positive integer that has exactly 75 divisors.

-----Note-----
When a positive integer A divides a positive integer B, A is said to a divisor of B.
For example, 6 has four divisors: 1, 2, 3 and 6.

-----Constraints-----
 - 1 \leq N \leq 100
 - N is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the number of the Shichi-Go numbers that are divisors of N!.

-----Sample Input-----
9

-----Sample Output-----
0

There are no Shichi-Go numbers among the divisors of 9! = 1 \times 2 \times ... \times 9 = 362880.
"""

import math
from collections import defaultdict
import numpy as np

def count_shichi_go_numbers(N):
    dic = defaultdict(lambda: 0)
    
    # Calculate the prime factorization of each number from 2 to N
    for i in range(2, N + 1):
        sqrt = math.floor(i ** 0.5)
        for j in range(2, sqrt + 1):
            if not i % j:
                count = 0
                while i % j == 0:
                    count += 1
                    i //= j
                dic[j] += count
        if i > 1:
            dic[i] += 1
    
    # Get the counts of each prime factor
    values = np.array(list(dic.values()))
    
    # Calculate the number of Shichi-Go numbers
    v1 = len(values[values >= 2])
    v2 = len(values[values >= 4])
    v = v2 * (v2 - 1) // 2 * (v1 - 2)
    v3 = len(values[values >= 24])
    v += v3 * (v1 - 1)
    v4 = len(values[values >= 14])
    v += v4 * (v2 - 1)
    v5 = len(values[values >= 74])
    v += v5
    
    return v