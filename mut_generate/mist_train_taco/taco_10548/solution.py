"""
QUESTION:
Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s. Output your answer modulo 10^9 + 7.
Example 1:
Input:
N = 3
Output: 5
Explanation: 5 strings are (000,
001, 010, 100, 101).
Example 2:
Input:
N = 2
Output: 3
Explanation: 3 strings are
(00,01,10).
Your Task:
Complete the function countStrings() which takes single integer n, as input parameters and returns an integer denoting the answer. You don't to print answer or take inputs. 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
"""

def count_distinct_binary_strings(n: int) -> int:
    mod = 10 ** 9 + 7
    if n == 0:
        return 1
    if n == 1:
        return 2
    
    l = [0] * (n + 1)
    l[0] = 1
    l[1] = 2
    
    for i in range(2, n + 1):
        l[i] = (l[i - 1] + l[i - 2]) % mod
    
    return l[n]