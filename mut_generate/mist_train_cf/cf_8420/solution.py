"""
QUESTION:
Create a function named `remove_duplicates` that takes a list of integers as input. The function should modify the input list in-place to only include unique elements, without using any built-in functions or libraries for counting or checking uniqueness, or any additional data structures or variables. The function should achieve a time complexity of O(n) and a space complexity of O(1), and it should return the modified list with unique elements.
"""

def remove_duplicates(nums):
    # Sort the list in-place
    nums.sort()
    
    # Initialize two pointers
    left = 0
    right = 1
    
    # Iterate through the list
    while right < len(nums):
        # If the current element is not equal to the previous element
        if nums[right] != nums[left]:
            # Move the left pointer one step forward
            left += 1
            # Update the value at the new position with the current element
            nums[left] = nums[right]
        
        # Move the right pointer one step forward
        right += 1
    
    # Return the list up to the left pointer (inclusive)
    return nums[:left+1]