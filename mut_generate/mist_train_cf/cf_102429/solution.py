"""
QUESTION:
Write a function fourSum(nums, k) that takes a list of integers nums and a target integer k as input. The function should return True if there exist exactly four numbers in the list whose sum is equal to k, and False otherwise. The list contains at least four integers.
"""

def fourSum(nums, k):
    # Sort the list in ascending order
    nums.sort()
    
    # Iterate through all possible combinations of four numbers
    for i in range(len(nums)-3):
        for j in range(i+1, len(nums)-2):
            # Use two pointers to find the other two numbers
            left = j + 1
            right = len(nums) - 1
            
            while left < right:
                # Calculate the sum of four numbers
                four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                
                if four_sum == k:
                    return True
                elif four_sum < k:
                    left += 1
                else:
                    right -= 1
    
    return False