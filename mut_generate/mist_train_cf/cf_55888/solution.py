"""
QUESTION:
Create a function `reverse_array_and_average` that takes a list of numbers as input and returns two lists. The first list contains the input numbers in reverse order, and the second list contains the running average of the reversed numbers. The running average at each index is calculated as the sum of all the current elements divided by the count of elements so far in the reversed list. The function should not use built-in or external library functions, including the `reverse` or `reversed` function in Python.
"""

def reverse_array_and_average(array):
    # Initialize the reversed array and running average lists
    reversed_array = []
    running_average = []

    # Loop backwards over the length of the array
    for i in range(len(array), 0, -1):
        # Add the current element to the reversed array
        reversed_array.append(array[i - 1])
        
        # Calculate the running average
        avg = sum(reversed_array) / len(reversed_array)
        running_average.append(avg)
    
    return reversed_array, running_average