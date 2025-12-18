"""
QUESTION:
Create a function named `calc_properties` that takes a list of integers as input and returns the minimum, maximum, and average of the list. The function should not use the built-in `min()`, `max()`, or `len()` functions. It should also handle the cases where the input list is empty or contains non-integer values. The function should print and return the minimum, maximum, and average of the list.
"""

def calc_properties(num_list):
    if not all(isinstance(num, int) for num in num_list):
        return "Error: List contains non-integer values."

    if not num_list:
        return "Error: List is empty."

    minNum, maxNum, sumNum = num_list[0], num_list[0], 0

    for num in num_list:
        if num < minNum:
            minNum = num
        if num > maxNum:
            maxNum = num
        sumNum += num

    avgNum = sumNum / len(num_list)

    print("Minimum: ", minNum)
    print("Maximum: ", maxNum)
    print("Average: ", avgNum)

    return minNum, maxNum, avgNum