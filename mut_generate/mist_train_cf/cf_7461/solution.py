"""
QUESTION:
Write a function named `find_four_elements` that takes a list of integers `nums` and a target value `target` as input, and returns all possible combinations of four elements in the list whose sum equals the target value. The function should have a time complexity of O(n^4) and a space complexity of O(n), where n is the length of the input list, and should handle cases where the input list contains negative integers.
"""

def find_four_elements(nums, target):
    # Sort the input list in ascending order
    nums.sort()
    
    # Initialize an empty list to store the combinations
    combinations = []
    
    # Iterate through each possible combination of four elements
    for i in range(len(nums)-3):
        for j in range(i+1, len(nums)-2):
            for k in range(j+1, len(nums)-1):
                for l in range(k+1, len(nums)):
                    # Check if the sum of the four elements is equal to the target value
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        combinations.append([nums[i], nums[j], nums[k], nums[l]])
    
    # Return the list of combinations
    return combinations