"""
QUESTION:
Create a function `print_third_elements` that takes an array and an index as parameters. The function should print every third element in the array, starting from the index, and skip the elements that are divisible by 2. The function should terminate once it has iterated through the entire array. Implement the solution using recursion instead of a traditional loop.
"""

def print_third_elements(array, index):
    if index >= len(array):  
        return

    if (index + 1) % 3 == 0 and array[index] % 2 == 0:  
        print_third_elements(array, index + 1)
    else:
        if (index + 1) % 3 == 0:
            print(array[index])
        print_third_elements(array, index + 1)