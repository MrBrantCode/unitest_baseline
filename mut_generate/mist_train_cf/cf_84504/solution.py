"""
QUESTION:
Create a function `multiplyDistinct` that takes a list of elements as input and returns the product of its distinct numerical elements (integers and floats), ignoring non-numerical elements. The function should handle lists containing duplicate elements and non-numerical elements.
"""

def multiplyDistinct(lst):
    # Get the distinct elements using set
    distinct_elements = set(lst)

    # Initialize the multiplication result as 1
    product = 1

    # Multiply each distinct element
    for num in distinct_elements:
        if isinstance(num, (int, float)):  # Check if element is a number
            product *= num

    return product