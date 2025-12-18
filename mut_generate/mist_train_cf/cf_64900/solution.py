"""
QUESTION:
Write a function named `multiply` that takes a list of integers as input, calculates the product of odd numbers located at even indices, and returns the result. The function should enforce the following constraints:
- The input list must be non-empty.
- All elements in the list must be integers.
- No element in the list should exceed 100.
- The final product should not exceed 5000.
- If any of these constraints are violated, return an error message describing the issue. If an unexpected exception occurs, return the exception as a string.
"""

def multiply(lst):
    """Given a non-empty list of integers lst, perform multiple steps calculation to find the product of odd elements located at even indices. Ensure none of the elements in the list exceeds 100 and that you handle possible exceptions. Additionally, guarantee the final product does not exceed 5000.

    """
    if not lst:    # if list is empty 
        return "Input list should not be empty."
    if not all(type(i) == int for i in lst):    # if list has non-integer elements 
        return "All elements of the input list should be integer."
    if not all(0 <= i <= 100 for i in lst):    # if list has elements exceeding 100
        return "Elements of the list should not exceed 100."
    try:
        product = 1
        for i in range(0, len(lst), 2):    # skipping 1 element i.e., considering elements at even indices
            if lst[i] % 2 != 0:    # if the element is odd
                product *= lst[i]
                if product > 5000:    # if the product exceeds 5000
                    return "Product exceeded 5000."
        return product
    except Exception as e:
        return str(e)