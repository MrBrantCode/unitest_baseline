"""
QUESTION:
Write a function named `find_max_min` that takes a list of numbers as input. The function should find the maximum and minimum numbers in the list and return them. It should also find the second largest and second smallest numbers in the list. The function should handle empty lists, non-numeric values, negative numbers, and lists with duplicate numbers. If the list is empty, the function should print a message indicating that the list is empty. If the list contains non-numeric values, the function should print a message indicating that the list contains non-numeric values. If all numbers in the list are the same, the function should print a message indicating that all numbers are the same. The function should use a loop to iterate through the list and compare each number with the maximum and minimum values found so far. The function should initialize the maximum value as negative infinity and the minimum value as positive infinity.
"""

def find_max_min(numbers):
    if len(numbers) == 0:
        print("The list is empty.")
        return

    max_value = float('-inf')
    min_value = float('inf')
    second_max = float('-inf')
    second_min = float('inf')
    is_duplicate = True

    for num in numbers:
        if not isinstance(num, (int, float)):
            print("The list contains non-numeric values.")
            return

        if num > max_value:
            second_max = max_value
            max_value = num
        elif num > second_max and num != max_value:
            second_max = num

        if num < min_value:
            second_min = min_value
            min_value = num
        elif num < second_min and num != min_value:
            second_min = num

        if num != max_value:
            is_duplicate = False

    if is_duplicate:
        print("All numbers in the list are the same.")
    else:
        print("Maximum number:", max_value)
        print("Minimum number:", min_value)
        print("Second largest number:", second_max)
        print("Second smallest number:", second_min)