"""
QUESTION:
Create a function `calculate_average` that takes a list of numbers as input and returns the average of all numeric elements. The function should handle empty input lists and non-numeric elements by printing an error or warning message and excluding them from the calculation. If the list is empty or contains no numeric elements, the function should return `None`.
"""

def calculate_average(numbers):
    # check if input list is empty
    if not numbers:
        print("Error: The list is empty.")
        return None

    sum = 0
    num_elements = 0  # counter for number of numeric elements

    for number in numbers:
        # check if element is numeric 
        if isinstance(number, (int, float)):
            sum += number
            num_elements += 1
        else:
            print(f"Warning: The element {number} is not a number. It is skipped.")

    # check if all elements were non-numeric
    if num_elements == 0:
        print("Error: The list doesn't contain any numeric values.")
        return None
    else:
        return sum / num_elements