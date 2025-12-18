"""
QUESTION:
Create a function `get_positive_multiply_and_sort(l: list, n: int)` that filters out only positive numbers from the input list `l`, multiplies them by a given integer `n`, and returns the sorted list in ascending order. Implement a helper function `multiply_elements(l: list, multiplier: int)` to multiply the positive numbers by the given multiplier, and another helper function `swap_elements(l: list, index1: int, index2: int)` for sorting elements. The sorting algorithm should be implemented manually (not using built-in sorting functions).
"""

def get_positive_multiply_and_sort(l: list, n: int):
    """Return only positive numbers in the list multiplied by n and sorted in ascending order."""
    
    def multiply_elements(l: list, multiplier: int):
        """Create a helper function to multiply the positive numbers by the given multiplier."""
        return [i * multiplier for i in l]

    def swap_elements(l: list, index1: int, index2: int):
        """Implement a helper function for sorting elements."""
        l[index1], l[index2] = l[index2], l[index1]

    positive_nums = [num for num in l if num > 0]
    multiplied_nums = multiply_elements(positive_nums, n)

    # Sorting: Implementing the Bubble Sort algorithm
    for i in range(len(multiplied_nums)):
        for j in range(len(multiplied_nums) - i - 1):
            if multiplied_nums[j] > multiplied_nums[j + 1]:
                swap_elements(multiplied_nums, j, j + 1)

    return multiplied_nums