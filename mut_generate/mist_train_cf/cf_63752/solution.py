"""
QUESTION:
Write a function `calculate_average_and_sort` that accepts a list of arrays as input. Each array consists of multiple integers. Calculate the average value of elements for each array without using the in-built average function. If an array is empty, consider its average as 0. Return a list of these averages in ascending order.
"""

def calculate_average_and_sort(arrays):
    averages = []
    for array in arrays:
        if len(array) != 0:  
            sum = 0
            for num in array:
                sum += num  
            averages.append(sum / len(array))  
        else:  
            averages.append(0)

    averages.sort()
    return averages