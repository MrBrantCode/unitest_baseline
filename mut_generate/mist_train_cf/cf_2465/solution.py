"""
QUESTION:
Write a function `transform_list` that takes a list of integers as input and returns a new list. The function should apply the following transformations: 
- square each positive even number
- cube each negative odd number
- replace 0 with the string "zero"
- replace any other non-numeric value or integer outside the range of -1000 to 1000 (inclusive) with the string "unknown"
"""

def transform_list(nums):
    transformed_nums = []
    
    for num in nums:
        if isinstance(num, int):
            if num == 0:
                transformed_nums.append("zero")
            elif num >= -1000 and num <= 1000:
                if num > 0 and num % 2 == 0:
                    transformed_nums.append(num ** 2)
                elif num < 0 and num % 2 != 0:
                    transformed_nums.append(num ** 3)
                else:
                    transformed_nums.append("unknown")
            else:
                transformed_nums.append("unknown")
        else:
            transformed_nums.append("unknown")
    
    return transformed_nums