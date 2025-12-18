"""
QUESTION:
Write a function named `second_largest_even_code` that takes a list of integers as input and returns a tuple containing the second largest even integer and the mean of all even integers. The function should not use built-in functions and should handle both positive and negative integers. If there are less than two even integers in the list, the function should return the second largest even integer as negative infinity. If there are no even integers in the list, the function should return "N/A" for the mean.
"""

def second_largest_even_code(L):
    max1, max2 = float('-inf'), float('-inf')
    count, sum = 0, 0
    for x in L:
        if x % 2 == 0:
            count += 1
            sum += x
            if x > max1:
                if max1 != max2:  
                    max2 = max1
                max1 = x
            elif x > max2 and x != max1:
                max2 = x
    return max2, "Mean:" + str(sum/count) if count != 0 else "N/A"