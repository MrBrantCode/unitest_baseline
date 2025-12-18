"""
QUESTION:
Create a function `second_smallest_odd_and_second_largest_even` that takes a list of integers `l` as input. The function should return a tuple where the first element is the second smallest odd number in the list, and the second element is the second largest even number in the list. If the list does not contain at least two odd numbers or at least two even numbers, the corresponding element in the tuple should be `None`.
"""

def second_smallest_odd_and_second_largest_even(l: list):
    min1, min2, max1, max2 = float('inf'), float('inf'), -float('inf'), -float('inf')
    odd_count, even_count = 0, 0

    for x in l:
        if x % 2 != 0:
            odd_count += 1
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x
        else:
            even_count += 1
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x
    
    res = [min2 if odd_count > 1 else None, max2 if even_count > 1 else None]
    return tuple(res)