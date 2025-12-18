"""
QUESTION:
Find the highest sum that can be obtained by including at most three different members from an array of positive integers such that no two members have the same index and the sum is divisible by 4. Implement a function named max_sum_divisible_by_four with one parameter: nums, a list of positive integers.
"""

def max_sum_divisible_by_four(nums):
    """
    This function calculates the highest sum that can be obtained by including at most three different members 
    from an array of positive integers such that no two members have the same index and the sum is divisible by 4.
    
    Parameters:
    nums (list): A list of positive integers.
    
    Returns:
    int: The highest sum that can be obtained.
    """
    max_sum = 0
    num1 = 0
    num2 = 0
    num3 = 0
    
    # Check for single elements that are divisible by 4
    for num in nums:
        if num % 4 == 0:
            max_sum = max(max_sum, num)
            
    # Check for pairs of elements that are divisible by 4
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) % 4 == 0:
                max_sum = max(max_sum, nums[i] + nums[j])
                
    # Check for triplets of elements that are divisible by 4
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) % 4 == 0:
                    max_sum = max(max_sum, nums[i] + nums[j] + nums[k])
                    
    return max_sum