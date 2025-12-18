"""
QUESTION:
Write a recursive function `separate_numbers` that takes a list of strings representing numbers as input. The function should return three separate lists: one for positive numbers, one for negative numbers, and one for zeroes. The function should ignore any non-numeric inputs.
"""

def separate_numbers(nums):
    """
    Recursively separate a list of strings representing numbers into three lists: 
    one for positive numbers, one for negative numbers, and one for zeroes.

    Args:
    nums (list): A list of strings representing numbers.

    Returns:
    tuple: A tuple containing three lists: positive numbers, negative numbers, and zeroes.
    """
    def helper(nums, pos, neg, zero):
        if not nums:   # base case: no more numbers to separate
            return pos, neg, zero
        else:
            try:   # try to convert the first element to a number
                num = float(nums[0])
            except ValueError:   # can't convert, skip this element
                return helper(nums[1:], pos, neg, zero)
                
            # add the number to the correct list
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
            else:
                zero.append(num)
            
            # recursively process the rest of the list
            return helper(nums[1:], pos, neg, zero)

    return helper(nums, [], [], [])