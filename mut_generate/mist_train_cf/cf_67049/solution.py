"""
QUESTION:
Create a function `second_highest_even_element` that takes a list of integers as input and returns a tuple containing the second highest even number in the list and the mean of all even numbers. The function should handle negative numbers and consider the case where the highest even number appears more than once.
"""

def second_highest_even_element(numbers: list):
    # Initialize to negative infinity
    max1, max2 = float('-inf'), float('-inf')
    mean, even_count = 0, 0
    for x in numbers:
        if x % 2 == 0:
            even_count += 1
            mean += x
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2 and x != max1:
                max2 = x
    if even_count > 1:
        mean /= even_count
        return max2, mean
    else:
        return max2, None