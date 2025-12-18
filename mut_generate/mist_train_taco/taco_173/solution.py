"""
QUESTION:
You are given an integer array nums that may contain duplicates. Your task is to return all possible subsets. Return only unique subsets and they can be in any order.
Example: 
Input: 
nums = [1,2,2] 
Output: 
[[],[1],[1,2],[1,2,2],[2],[2,2]]
Explanation: 
We can have subsets ranging from length 0 to 3. which are listed above. Also the subset [1,2] appears twice but is printed only once as we require only unique subsets.
Your Task:
Complete the function vector> printUniqueSubset(), which takes  a vector nums and return a vector of vector consisting of all unique subsets.
Expected Time Complexity: O(K2^{N}).
Expected Auxiliary Space: O(K2^{N}).
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

def generate_unique_subsets(nums):
    n = len(nums)
    nums.sort()
    ans = []

    def solve(i, temp):
        ans.append(temp[:])
        for j in range(i, n):
            if j > i and nums[j] == nums[j - 1]:
                continue
            temp.append(nums[j])
            solve(j + 1, temp)
            temp.pop()
    
    solve(0, [])
    return ans