"""
QUESTION:
Create a function named `sort_and_sum_even` that takes a list of integers as input. The function should sort the list in descending order, calculate the sum of all non-negative even numbers, and return a message with the sorted list and the sum of even numbers. If the list does not contain any non-negative even numbers, the function should return a message stating that there are no even numbers in the list. The function should also handle any potential errors that may occur during the process and provide an error message if necessary.
"""

def sort_and_sum_even(numbers):
    try:
        numbers.sort(reverse=True)
        sum_even = sum(num for num in numbers if num >= 0 and num % 2 == 0)
        if sum_even == 0:
            return "There are no even numbers in the list."
        else:
            return f"Sorted list in descending order: {numbers}\nSum of even numbers: {sum_even}"
    except Exception as e:
        return f"An error occurred: {str(e)}"