"""
QUESTION:
Given an integer N, the task is to find out M increasing numbers such that the sum of M numbers is equal to N and the GCD of these M numbers is maximum among all possible combinations (or series) of M numbers.
Note: If two or more such series are possible then return the series which has smallest first term.
Example 1:
Input: N = 24, M = 3
Output: 4 8 12
Explanation: (3, 6, 15) is also a series 
of M numbers which sums to N, but gcd = 3
(4, 8, 12) has gcd = 4 which is the maximum
possible.
Example 2:
Input: N = 6, M = 4
Output: -1
Explanation: It is not possible as the 
least GCD sequence will be 1+2+3+4 which
is greater then n, hence print -1.
Your Task:  
You dont need to read input or print anything. Complete the function M_sequence() which takes N and M as input parameter and returns th series of M numbers and if there are no series exist returns -1.
Expected Time Complexity: O(sqrt(n))
Expected Auxiliary Space: O(n)
Constraints:
1 <= N <=10^{5}
"""

import math

def find_max_gcd_sequence(N, M):
    # Calculate the minimum sum of the first M natural numbers
    min_sum = (1 + M) * M // 2
    
    # If the minimum sum is greater than N, return -1
    if min_sum > N:
        return -1
    
    # Initialize the maximum GCD found
    max_gcd = -1
    
    # Iterate from the square root of N down to 1 to find the maximum GCD
    for i in range(int(math.sqrt(N)), 0, -1):
        if N % i == 0:
            d = N // i
            if d * min_sum <= N:
                max_gcd = max(max_gcd, d)
            if i * min_sum <= N:
                max_gcd = max(max_gcd, i)
    
    # If no valid GCD was found, return -1
    if max_gcd == -1:
        return -1
    
    # Generate the sequence with the found maximum GCD
    ans = []
    i = 1
    while len(ans) < M - 1:
        ans.append(i * max_gcd)
        N -= i * max_gcd
        i += 1
    ans.append(N)
    
    return ans