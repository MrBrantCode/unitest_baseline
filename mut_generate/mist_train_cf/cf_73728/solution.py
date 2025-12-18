"""
QUESTION:
Write a function called `validate_sorting` that takes an unsorted array as input and returns a string indicating whether the sorting algorithm is accurate. The function should compare the sorted array with the original unsorted array to determine accuracy. The array [3, 2, 1] will be used for testing the function.
"""

def validate_sorting(unsorted_array):
    sorted_array = sorted(unsorted_array)
    if sorted_array == unsorted_array:
        return "Algorithm is accurate"
    else:
        return "Algorithm is not accurate"