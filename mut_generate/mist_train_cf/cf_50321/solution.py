"""
QUESTION:
Develop a function called `total_numeric_elements` that calculates the cumulative total of all numerical elements within a potentially nested array structure. The function should ignore non-numerical elements when calculating the total sum and be able to handle arrays nested within other arrays. The function should take a single argument `arr` representing the input array.
"""

def total_numeric_elements(arr):
    total_sum = 0
    for element in arr:
        if type(element) == list:
            total_sum += total_numeric_elements(element)
        elif type(element) == int or type(element) == float:
            total_sum += element
    return total_sum