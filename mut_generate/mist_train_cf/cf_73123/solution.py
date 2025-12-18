"""
QUESTION:
Write a function named `cubed_product` that calculates the product of the cubical values of individual integers within a given list. The list should contain only integers between -10 and 10. Implement exception handling to handle potential errors, including non-integer values and input outside the specified range.
"""

def cubed_product(lst):
    """
    Function to calculate the product of cubical values of the elements from a list.
    """
    try:
        # Initialize the product as 1 (neutral element for multiplication)
        product = 1

        # Iterate through the list
        for num in lst:

            # Check if the number is an integer and between -10 and 10
            if type(num) != int or num < -10 or num > 10:
                return "Invalid input: All elements should be integers between -10 and 10."

            # Cube the number and multiply it with the product
            product *= num ** 3

        # Return the final product
        return product
    except Exception as e:
        # In case of any other exception, print the exception message
        return f"An error occurred: {e}"