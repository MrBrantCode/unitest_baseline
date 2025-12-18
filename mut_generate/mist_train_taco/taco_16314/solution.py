"""
QUESTION:
Takahashi has N balls. Initially, an integer A_i is written on the i-th ball.
He would like to rewrite the integer on some balls so that there are at most K different integers written on the N balls.
Find the minimum number of balls that Takahashi needs to rewrite the integers on them.

-----Constraints-----
 - 1 \leq K \leq N \leq 200000
 - 1 \leq A_i \leq N
 - All input values are integers.

-----Input-----
Input is given from Standard Input in the following format:
N K
A_1 A_2 ... A_N

-----Output-----
Print the minimum number of balls that Takahashi needs to rewrite the integers on them.

-----Sample Input-----
5 2
1 1 2 2 5

-----Sample Output-----
1

For example, if we rewrite the integer on the fifth ball to 2, there are two different integers written on the balls: 1 and 2.
On the other hand, it is not possible to rewrite the integers on zero balls so that there are at most two different integers written on the balls, so we should print 1.
"""

from collections import Counter

def min_balls_to_rewrite(N, K, A):
    # Count the frequency of each integer on the balls
    frequency_count = Counter(A)
    
    # Sort the frequency count by the frequency in ascending order
    sorted_frequency = sorted(frequency_count.items(), key=lambda x: x[1])
    
    # Calculate the number of different integers that need to be reduced
    num_to_reduce = max(len(sorted_frequency) - K, 0)
    
    # Calculate the minimum number of balls to rewrite
    ans = 0
    for i in range(num_to_reduce):
        ans += sorted_frequency[i][1]
    
    return ans