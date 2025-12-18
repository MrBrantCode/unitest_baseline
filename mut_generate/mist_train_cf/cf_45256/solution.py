"""
QUESTION:
Implement a function `switch_sequence(nums)` that takes a list of integers as input. The function should return the sum of the unique numbers in the list, where each number is alternately added or subtracted from the sum, starting with addition. If the list contains any non-positive numbers or None values, the function should return None. The input list should only contain unambiguous positive integers.
"""

def switch_sequence(nums):
    # Check for None in the list and drop it
    if any(i is None for i in nums):
        return None
    # Check for negative or zero numbers and drop them
    elif any(i <= 0 for i in nums):
        return None
    else:
        # Remove repetition by converting list to set
        nums_set = set(nums)
    
        # Initialize toggle and summation
        toggle = 1
        summation = 0
        
        # Loop over the set and recursively switch between addition and subtraction
        for num in nums_set:
            summation += toggle * num
            toggle *= -1  # Switch between 1 and -1

        return abs(summation)