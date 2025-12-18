"""
QUESTION:
Write a function `getSecondMax` that takes a list of numbers `a` as input and prints the second highest value in the list. If the list contains duplicate values, the function should still print the correct second highest value. The list must contain at least 2 values.
"""

def getSecondMax(a):
    if len(a) < 2:
        print("Error: The list must contain at least 2 values")
        return

    max_value = float('-inf')
    second_max_value = float('-inf')

    for num in a:
        if num > max_value:
            second_max_value = max_value
            max_value = num
        elif num > second_max_value and num != max_value:
            second_max_value = num

    print(second_max_value)