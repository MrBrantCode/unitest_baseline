"""
QUESTION:
Given two integers L and R find (number of composites - number of primes) between the range L and R (both inclusive).
Example 1:
Input: L = 4, R = 6
Output: 1
Explanation: Composite no. are 4 and 6.
And prime is 5.
Example 2:
Input: L = 4, R = 4
Output: 1
Explanation: There is no prime no. in [L,R]
 
Your Task:
You don't need to read or print anything. Your task is to complete the function Count() which takes L and R as input parameter and returns difference between no. of composites and primes between [L,R].
 
Expected Time Complexity: O(nlog(n)) where n = R - L + 1
Expected Space Complexity: O(n)
 
Constraints:
1 <= L <= R <= 10^{5}
"""

def count_composites_minus_primes(L, R):
    primes = [1] * (R + 1)
    primes[0] = primes[1] = 0
    p = 2
    while p * p <= R:
        if primes[p]:
            for i in range(p * p, R + 1, p):
                primes[i] = 0
        p += 1
    (cnt, cnt1) = (0, 0)
    for i in range(L, R + 1):
        if primes[i]:
            cnt += 1
        else:
            cnt1 += 1
    if L == 1:
        return cnt1 - cnt - 1
    return cnt1 - cnt