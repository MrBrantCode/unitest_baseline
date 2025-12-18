"""
QUESTION:
Design a function called `product_list_except_self` that takes a list of integers as input and returns a new list. The function should calculate the product of all numbers in the input list excluding the number at the same index for each element in the output list. If the input list contains a zero, the product of all numbers excluding zero should be returned at the index where zero is located, and zeros should be returned at all other indices.
"""

def product_list_except_self(nums):
    if 0 in nums:
        product_all = 1
        for num in nums:
            if num != 0:
                product_all *= num

        return [product_all if num == 0 else 0 for num in nums]
    else:
        product_all = 1
        for num in nums:
            product_all *= num

        return [product_all // num for num in nums]