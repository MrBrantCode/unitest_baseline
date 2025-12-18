"""
QUESTION:
Given is an integer sequence A_1, ..., A_N of length N.
We will choose exactly \left\lfloor \frac{N}{2} \right\rfloor elements from this sequence so that no two adjacent elements are chosen.
Find the maximum possible sum of the chosen elements.
Here \lfloor x \rfloor denotes the greatest integer not greater than x.

-----Constraints-----
 - 2 \leq N \leq 2\times 10^5
 - |A_i|\leq 10^9
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
A_1 ... A_N

-----Output-----
Print the maximum possible sum of the chosen elements.

-----Sample Input-----
6
1 2 3 4 5 6

-----Sample Output-----
12

Choosing 2, 4, and 6 makes the sum 12, which is the maximum possible value.
"""

def max_sum_non_adjacent(n, a):
    dp = [0]
    sum_odd = a[0]
    dp.append(0)
    
    for i in range(2, n + 1):
        if i % 2 == 1:
            sum_odd += a[i - 1]
            dp.append(max(dp[i - 1], dp[i - 2] + a[i - 1]))
        else:
            dp.append(max(sum_odd, a[i - 1] + dp[i - 2]))
    
    return dp[n]