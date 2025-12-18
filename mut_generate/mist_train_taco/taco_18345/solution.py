"""
QUESTION:
Given a number X find the total numbers A such that A XOR X >= X,  and 1<=A<=X.
 
Example 1:
Input: 10
Output: 5
Explanation: Calculating XOR of 10 with
{1, 4, 5, 6, 7} give values greater than 
equal to 10.
Example 2:
Input: 5
Output: 2
Explanation: Calculating XOR of 5 with 
{2, 3} give values greater than 5.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function maximize_xor_count() which takes X as input parameter and returns total numbers A.
 
Expected Time Complexity: O(log(n))
Expected Space Complexity: O(1)
 
Constraints:
1 <= X <= 10^{8}
"""

def maximize_xor_count(X: int) -> int:
    ans = 0
    k = 1
    while X:
        if X & 1 == 0:
            ans += k
        X >>= 1
        k <<= 1
    return ans