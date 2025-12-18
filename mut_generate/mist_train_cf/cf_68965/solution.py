"""
QUESTION:
Implement the function `subarraySum(nums, k)` to return the total number of continuous subarrays in `nums` whose sum equals `k`. The function should not use any built-in functions or libraries. The length of `nums` is between 1 and 2 * 10^4, and the range of `nums[i]` and `k` is between -10^3 and 10^3, and between -10^7 and 10^7, respectively. The function should have a time complexity better than O(n^2).
"""

def subarraySum(nums, k):
    count, running_sum = 0, 0
    sum_dict = {0: 1}  
      
    for i in range(len(nums)):
        running_sum += nums[i]
        
        if (running_sum - k) in sum_dict:
            count += sum_dict[running_sum - k]
            
        if running_sum in sum_dict:
            sum_dict[running_sum] += 1
        else:
            sum_dict[running_sum] = 1 
     
    return count