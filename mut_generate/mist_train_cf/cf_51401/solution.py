"""
QUESTION:
Write a function `largest_smallest_integer` that takes a list of integers as input and returns a tuple of six numbers representing the highest and smallest negative and non-negative even and odd numbers in the list. If the list does not contain any number that satisfies any of these criteria, the corresponding position in the returned tuple should be None.
"""

def largest_smallest_integer(lst):
    highest_neg_even = smallest_neg_even = highest_non_neg_even = smallest_non_neg_even = smallest_neg_odd = highest_non_neg_odd = None

    for num in lst:
        if num % 2 == 0:  
            if num < 0:  
                if highest_neg_even is None or highest_neg_even < num:  
                    highest_neg_even = num
                if smallest_neg_even is None or smallest_neg_even > num:  
                    smallest_neg_even = num
            else:  
                if highest_non_neg_even is None or highest_non_neg_even < num:  
                    highest_non_neg_even = num
                if smallest_non_neg_even is None or smallest_non_neg_even > num:  
                    smallest_non_neg_even = num
        else:  
            if num < 0:  
                if smallest_neg_odd is None or smallest_neg_odd > num:  
                    smallest_neg_odd = num
            else:  
                if highest_non_neg_odd is None or highest_non_neg_odd < num:  
                    highest_non_neg_odd = num

    return highest_neg_even, highest_non_neg_even, smallest_neg_even, smallest_non_neg_even, smallest_neg_odd, highest_non_neg_odd