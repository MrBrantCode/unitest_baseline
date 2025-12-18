"""
QUESTION:
Create a function called `custom_sort_unique` that takes an array of integers as input and returns a tuple. The function should first remove duplicates from the array and sort the unique elements in ascending order. Then, it should check if the sorted unique elements are in the correct order that can be achieved by reversing subarrays and deleting elements. If they are, the function returns `True` and the count of total operations (i.e., the number of removed duplicates) required to sort and remove duplicates. If they are not, the function returns `False` and 0 operation count. If the input array is empty, the function should return `True` and 0 operation count. Reversing a subarray or deleting an element is counted as a single operation.
"""

def custom_sort_unique(numbers):
    unique_numbers = set()
    operation_count = 0
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.add(number)
        else:
            operation_count += 1
    sorted_unique_numbers = sorted(list(unique_numbers))
    for i in range(len(sorted_unique_numbers) - 1):
        if sorted_unique_numbers[i] > sorted_unique_numbers[i + 1]:
            return False, 0
    return True, operation_count