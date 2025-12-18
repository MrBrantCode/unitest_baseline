"""
QUESTION:
Given an array of integers A[] of length N and an integer target.
You want to build an expression out of A by adding one of the symbols '+' and '-' before each integer in A and then concatenate all the integers.
	For example, if arr = {2, 1}, you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that can be built, which evaluates to target.
Example 1:
Input:
N = 5
A[] = {1, 1, 1, 1, 1}
target = 3
Output:
5
Explanation:
There are 5 ways to assign symbols to 
make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:
Input:
N = 1
A[] = {1}
target = 1
Output:
1
Your Task:
The task is to complete the function findTargetSumWays() which finds and returns the number of different expressions that can be built.
 
Expected Time Complexity: O(N*sum), where sum refers to the range of sum possible.
Expected Auxiliary Space: O(N).
 
Constraints:
1 ≤ N ≤ 20
0 ≤ A[i] ≤ 1000
0 <= sum(A[i]) <= 10^{4}
-1000 <= target <= 1000
"""

def find_target_sum_ways(nums, target):
    dp = {}
    n = len(nums)

    def helper(ind, tar):
        if ind == n and tar == target:
            return 1
        if ind == n:
            return 0
        if (ind, tar) in dp:
            return dp[(ind, tar)]
        take_plus = helper(ind + 1, tar - nums[ind])
        take_minus = helper(ind + 1, tar + nums[ind])
        dp[(ind, tar)] = take_plus + take_minus
        return dp[(ind, tar)]
    
    return helper(0, 0)