"""
QUESTION:
Mike is a seventh grade student and today is his birthday. He wishes to distribute a chocolate each among his friends. He already knows all of his friends have some chocolates with them.
All his friends stand in a straight line. Mike can take all the chocolates of any one of his friend. Find the minimum number of chocolate he should have from the starting so that he can end up in giving minimum of a chocolate each to all his friends. 
He will visit all his friends only once in the order 1,2, ... N.
 
Example 1:
Input: nums = {2, 3, 1, 2, 5, 2}
Output: 3
Explanation: If he takes the choclates of 
his 2nd friend. Then before coming to the 
2nd friend he needs 1 chocolate. Now 
including his 2nd friend he needs minimum 
of 2 chocolates after taking the chocolates 
of his 2nd friend. 
Example 2:
Input: nums = {1, 2, 3}
Output: 1
Explanation: If he takes the chocolates of his 
2nd friend then he only needs 1 chocolate.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function MinimumChocolate() which takes a list which contains the number of choclates his friends have initially and returns the minimum number of chocolates needed to distrubute minimum of a chocolate to every friend.
 
Expected Time Complexity:  O(N)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 100000
0 <= Every friend has chocolates <= 10000
"""

def minimum_chocolates(nums):
    ans = float('inf')
    n = len(nums)
    for i in range(n):
        curr = i
        curr += max(0, n - i - nums[i])
        ans = min(ans, curr)
    return ans