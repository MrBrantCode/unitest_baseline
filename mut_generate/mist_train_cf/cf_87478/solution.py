"""
QUESTION:
Define a function `transform_list` that takes a list of integers as input and returns a new list. The new list contains the square of each positive even number, the cube of each negative odd number, "zero" for the integer 0, and "unknown" for any other non-numeric value or any integer outside the range of -1000 to 1000 (inclusive).
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