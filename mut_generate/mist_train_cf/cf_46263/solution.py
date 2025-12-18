"""
QUESTION:
Write a function `second_smallest_odd_and_second_largest_even` that takes a list of integers as input and returns a tuple of two elements. The first element is the second smallest odd number in the list, and the second element is the second largest even number in the list. If there are less than two odd numbers or even numbers in the list, the corresponding element in the tuple should be `None`.
"""

def second_smallest_odd_and_second_largest_even(nums):
    min1, min2, max1, max2 = float('inf'), float('inf'), -float('inf'), -float('inf')
    odd_count, even_count = 0, 0

    for x in nums:
        if x % 2 != 0:
            odd_count += 1
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2 and x != min1:
                min2 = x
        else:
            even_count += 1
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2 and x != max1:
                max2 = x

    return (min2 if odd_count > 1 else None, max2 if even_count > 1 else None)