"""
QUESTION:
You are given array nums of n elements and integer K, and count the number of subarrays that has k odd numbers.
Example1:
Input:
n = 5
nums = [1,1,2,1,1]
k = 3
Output:
2
Explanation:
There are 2 subarrays with k odds [1,1,2,1] and [1,2,1,1]
Example 2:
Input:
n=3
nums = [2,4,6]
k = 1
Output:
0
Your Task:
You don't have to read input or print anything. Your task is to complete the function countSubarray() which takes the integer n and array nums and integer K as input and returns the count of subarray having k odds number.
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
Constraint:
1 <= n <= 50000
1 <= nums <= 105
1 <= k <=n
"""

def count_subarrays_with_k_odds(nums: list[int], k: int) -> int:
    # Convert the array to a binary form where odd numbers are 1 and even numbers are 0
    for i in range(len(nums)):
        nums[i] = nums[i] % 2
    
    # Dictionary to store the frequency of prefix sums
    sum_dict = {0: 1}
    current_sum = 0
    count = 0
    
    for num in nums:
        current_sum += num
        rem = current_sum - k
        
        if rem in sum_dict:
            count += sum_dict[rem]
        
        sum_dict[current_sum] = sum_dict.get(current_sum, 0) + 1
    
    return count