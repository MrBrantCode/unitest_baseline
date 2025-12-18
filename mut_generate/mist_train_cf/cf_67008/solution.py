"""
QUESTION:
Create a function `process_array(arr)` that takes an array of elements as input and returns the cumulative total, product, and average of the numeric elements in the array. The function should handle edge cases such as empty arrays, negative numbers, floating-point numbers, and large arrays efficiently. It should also handle non-numeric elements by skipping them and printing an error message. If the array is empty or contains no numeric elements, the function should return a clear message indicating this.
"""

def process_array(arr):
    """
    This function processes an array of elements and returns the cumulative total, 
    product, and average of the numeric elements in the array.

    Args:
        arr (list): A list of elements.

    Returns:
        tuple: A tuple containing the cumulative total, product, and average of the numeric elements.
        str: A message if the array is empty or contains no numeric elements.
    """

    if not arr:  # If the array is empty, we return a clear message
        return "The provided list is empty."

    total = 0
    product = 1
    count = 0
    for element in arr:
        if not isinstance(element, (int, float)):  # If the element is not a number, we skip it
            print(f"Error: {element} is not a number. Skipping this element.")
            continue
        total += element
        product *= element
        count += 1

    if count == 0:  # If all elements were non-numeric, we return a clear message
        return "There were no numeric elements in the list."
    
    average = total / count
    return total, product, average