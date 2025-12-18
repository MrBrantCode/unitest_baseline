"""
QUESTION:
Given 5 integers K, L, R, X, Y. Find whether there exists two integers A and B such that A / B = K where L ≤ A ≤ R and X ≤ B ≤ Y.
Example 1:
Input: K = 1, L = 1, R = 10
       X = 1, Y = 10
Output: 1
Explanation:
A = 1 , B = 1 exists such that L ≤ A ≤ R,
X ≤ B ≤ Y and A / B = K.
Note,there are other pairs present
Like A = 2, B = 2 etc which also satisfy 
the conditions.
Example 2:
Input: K = 1, L = 1,  R = 5
       X = 6, Y = 10
Output: 0
Explanation:
No such A and B exist that  satisfy all 
the conditions.
Your Task:
You don't need to read input or print anything. Your Task is to complete the function easyProblem() which takes 5 integers K, L, R,  X, and Y as input parameters and returns 1 if there exists two numbers that follow the above-given conditions. Otherwise, return 0.
Expected Time Complexity:O(N)
Expected Auxillary Space:O(1)
Constraints:
1≤ K, L, R, X, Y≤ 10^{6}
"""

def exists_divisible_pair(K, L, R, X, Y):
    left = X
    right = Y
    while left <= right:
        mid = (left + right) // 2
        A = K * mid
        if L <= A <= R:
            return 1
        elif A < L:
            left = mid + 1
        else:
            right = mid - 1
    return 0