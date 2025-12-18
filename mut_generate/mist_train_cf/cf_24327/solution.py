"""
QUESTION:
Create a function named `create_input_string` that takes two parameters: `nums` (a list of numbers) and `ops` (a list of operations). The function should combine the numbers and operations into a single string where each operation is placed between two numbers. The number of operations should be one less than the number of numbers, and there should not be an operation before the first number or after the last number.
"""

def create_input_string(nums, ops):
    input_str = ""
    
    for i in range(len(nums)):
        if i == 0:
            input_str += str(nums[i])
        else:
            input_str += ops[i - 1] + str(nums[i])
    
    return input_str