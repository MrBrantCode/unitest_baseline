"""
QUESTION:
Create a recursive function named `print_reversed` that takes an array and its index as input and prints the array elements in reverse order. The function should not use any built-in functions like `reversed` or slicing, and it should only use the provided index to traverse the array. The function should have a terminating condition to stop the recursion.
"""

def print_reversed(array, index):
    if index < 0:   # terminating condition
        return
    print(array[index])  # print current item
    print_reversed(array, index - 1)  # recursive call with the next index