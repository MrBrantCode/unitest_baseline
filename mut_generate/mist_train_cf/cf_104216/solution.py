"""
QUESTION:
Write a function `filter_and_sort` that takes a list of numbers as input, filters out the numbers that are not divisible by both 3 and 5, sorts the remaining numbers in descending order, and returns the filtered list along with the product of its elements. If the input list contains no numbers divisible by both 3 and 5, the function should return a message indicating this.
"""

def filter_and_sort(numbers):
    """Filters out numbers not divisible by both 3 and 5, sorts in descending order, 
    and returns the filtered list along with the product of its elements."""
    filtered_list = [num for num in numbers if num % 3 == 0 and num % 5 == 0]
    filtered_list.sort(reverse=True)
    if len(filtered_list) == 0:
        return "No numbers divisible by both 3 and 5 found in the list."
    product = 1
    for num in filtered_list:
        product *= num
    return filtered_list, product