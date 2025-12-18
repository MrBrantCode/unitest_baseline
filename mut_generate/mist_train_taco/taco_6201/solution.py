"""
QUESTION:
Given three integers x, y, and z, the task is to find the sum of all the numbers formed by 
having 4 at most x times, having 5 at most y times, and having 6 at most z times as a digit.
Note: Output the sum modulo 10^{9}+7.
Example 1:
Input: X = 1, Y = 1, Z = 1 
Output: 3675
Explanation: 4 + 5 + 6 + 45 + 54 + 56 
+ 65 + 46 + 64 + 456 + 465 
+ 546 + 564 + 645 + 654 = 3675
Example 2:
Input: X = 0, Y = 0, Z = 0
Output: 0
Explanation: No number can be formed
Your Task:  
You don't need to read input or print anything. Complete the function getSum() which takes X, Y and Z as input parameters and returns the integer value
Expected Time Complexity: O(X*Y*Z)
Expected Auxiliary Space: O(X*Y*Z)
Constraints:
0 ≤ X, Y, Z ≤ 60
"""

import numpy as np

def calculate_sum_of_numbers(x, y, z):
    N = 101
    mod = int(1000000000.0) + 7
    exactsum = np.zeros((N, N, N))
    exactnum = np.zeros((N, N, N))
    ans = 0
    exactnum[0][0][0] = 1
    
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i > 0:
                    exactsum[i][j][k] += (exactsum[i - 1][j][k] * 10 + 4 * exactnum[i - 1][j][k]) % mod
                    exactnum[i][j][k] += exactnum[i - 1][j][k] % mod
                if j > 0:
                    exactsum[i][j][k] += (exactsum[i][j - 1][k] * 10 + 5 * exactnum[i][j - 1][k]) % mod
                    exactnum[i][j][k] += exactnum[i][j - 1][k] % mod
                if k > 0:
                    exactsum[i][j][k] += (exactsum[i][j][k - 1] * 10 + 6 * exactnum[i][j][k - 1]) % mod
                    exactnum[i][j][k] += exactnum[i][j][k - 1] % mod
                ans += exactsum[i][j][k] % mod
                ans %= mod
    
    return int(ans)