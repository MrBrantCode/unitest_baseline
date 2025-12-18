"""
QUESTION:
Given an array of integers find the pair in the array with maximum GCD. Find the maximum possible GCD.
Example 1:
Input: N = 5, a[] = {1, 2, 3, 4, 5}
Output: 2
Explanation: Maximum gcd is GCD(2, 4)
= 2.
Ã¢â¬â¹Example 2:
Input: N = 3, a[] = {3, 5, 2}
Output: 1
Explanation: Maximum gcd is 1.
Your Task:  
Your task is to complete the function MaxGcd() which takes the N and list of N elements as inputs and returns the answer.
Expected Time Complexity: O(N * log N)
Expected Auxiliary Space: O(max(a_{i}))
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ a_{i} ≤ 10^{5}
"""

def find_max_gcd(a, n):
    if n < 2:
        return 0  # Edge case: if there are less than 2 elements, GCD is 0
    
    maxi = max(a)
    freq = [0] * (maxi + 1)
    
    for x in a:
        freq[x] += 1
    
    for i in range(maxi, 0, -1):
        cnt = 0
        for j in range(i, maxi + 1, i):
            cnt += freq[j]
        if cnt >= 2:
            return i
    
    return 1  # Default case if no valid GCD is found (though per problem constraints, this should not happen)