"""
QUESTION:
Calculate the product of distinct signs and the sum of distinct absolute values in a given array of non-zero integers, ignoring repetitive instances and zeros, and return None if the array is empty or contains a zero. 

The function `prod_signs(arr)` should take an array of non-zero integers as input and return the product of the sum of distinct absolute values and the product of distinct signs. If the array is empty or contains a zero, the function should return None.
"""

def prod_signs(arr):
    if not arr: return None
    distinct_signs_product = 1  # initial product of distinct signs
    distinct_absolute_sums = 0  # initial sum of distinct absolute values
    distinct_elements = set()  # a set to keep track of encountered distinct elements

    for n in arr:
        if n == 0:  # ignore 0 as per requirement
            return None  # whenever a 0 is encountered, the function should return None as per requirement
        absolute_value = abs(n)  # absolute value of the current number
        if absolute_value in distinct_elements:
            continue  # if this absolute value has been encountered before, ignore it
        distinct_elements.add(absolute_value)  # mark this absolute value as encountered
        sign = n/absolute_value  # sign of the current number
        distinct_signs_product *= sign  # update the product of distinct signs
        distinct_absolute_sums += absolute_value  # update the sum of distinct absolute values
      
    return distinct_signs_product*distinct_absolute_sums  # return the product as per requirement