"""
QUESTION:
Create a recursive function named `print_third_elements` that takes an array and an index as parameters. The function should print every third element in the array, starting from the second element (index 1). If the third element is divisible by 2, skip that iteration. The function should terminate once it has iterated through the entire array.
"""

def print_third_elements(array, index):
    if index >= len(array):  # base case: terminate once all elements have been iterated
        return

    if (index + 1) % 3 == 0 and array[index] % 2 == 0:  # skip iteration if third element is divisible by 2
        print_third_elements(array, index + 1)
    else:
        print(array[index])
        print_third_elements(array, index + 1)