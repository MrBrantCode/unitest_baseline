"""
QUESTION:
Write a function `mean(arr)` that calculates the mean of a given array of integers. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array. The function cannot use any built-in functions or libraries to calculate the mean. The input array can contain up to 10^6 integers. Additionally, the function can only use bitwise operations to perform arithmetic calculations.
"""

def mean(arr):
    n = len(arr)
    sum_val = 0
    
    for num in arr:
        add = sum_val
        carry = 0
        while num:
            sum_val = add ^ num
            carry = (add & num) << 1
            add = sum_val
            num = carry
    return sum_val / n