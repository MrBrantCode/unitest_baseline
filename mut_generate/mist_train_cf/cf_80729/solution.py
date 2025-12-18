"""
QUESTION:
Design a function `elusive_odd_and_even_totals` that takes an array of positive integers as input and returns a sorted array. The output array should contain all unique elements from the input array whose digits sum up to an odd number, plus one unique element whose digits sum up to an even number. If multiple even numbers exist, include the smallest one. If no even numbers exist, return only the odd numbers. The output array should be sorted in ascending order.
"""

def elusive_odd_and_even_totals(y):
    # to keep track of result
    even_num = None
    odd_nums = []     
    for num in set(y):    # iterating through unique elements
        digit_sum = sum(int(digit) for digit in str(num))  # sum of digits
        if digit_sum % 2 == 0:                # even
            if even_num is None:    
                even_num = num
            elif num < even_num:     # replace if a smaller is encountered
                even_num = num
        else:                        # odd
            odd_nums.append(num)
    odd_nums.sort()  
    if even_num is not None:    # even_num does not exist if all sums are odd
        odd_nums.append(even_num)
    return sorted(odd_nums)