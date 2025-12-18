"""
QUESTION:
You need to calculate the following sum over Q queries.:
Assume array to be 1-indexed.
 
Example 1:
Input: nums = {2, 3, 4, 5, 1, 6, 7},
Query = {{2, 4}, {2, 6}}
Output: {64, 230}
Explanation: For the 1st query,
(1^{2} * 3 + 2^{2} * 4 + 3^{2} * 5) = 64.
For the second query
(1^{2} * 3 + 2^{2} * 4 + 3^{2} * 5 + 4^{2} * 1 + 5^{2} * 6) = 
230
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function FindQuery() which takes nums and Query as input parameter and returns a list containg the answer modulo 10^{9} + 7 for each query.
 
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
 
Constraints:
1 <= n <= 10^{5}
1 <= nums[i] <= 10^{5}
1 <= no. of queries <= 10^{4}
"""

def calculate_query_sums(nums, queries):
    n = len(nums)
    m = len(queries)
    mod = 1000000007
    
    # Precompute prefix sums
    dp1 = [0] * (n + 1)
    dp2 = [0] * (n + 1)
    dp3 = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp1[i] = (dp1[i - 1] + nums[i - 1]) % mod
        dp2[i] = (dp2[i - 1] + i * nums[i - 1]) % mod
        dp3[i] = (dp3[i - 1] + i * i * nums[i - 1]) % mod
    
    results = []
    
    for query in queries:
        start = query[0]
        end = query[1]
        
        ans = dp3[end] - dp3[start - 1]
        ans += (start - 1) * (start - 1) * (dp1[end] - dp1[start - 1])
        ans += 2 * (1 - start) * (dp2[end] - dp2[start - 1])
        ans = ans % mod
        
        results.append(int(ans))
    
    return results