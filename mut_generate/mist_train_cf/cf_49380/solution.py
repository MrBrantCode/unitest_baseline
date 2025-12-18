"""
QUESTION:
Write a function `hex_product_finder` that takes a list of hexadecimal numbers and a target product as input, and returns a list of pairs of hexadecimal numbers from the input list that, when multiplied, result in the target product.
"""

def hex_product_finder(hex_list, target_product):
    """
    This function finds pairs of hexadecimal numbers in the input list that, when multiplied, result in the target product.

    Args:
        hex_list (list): A list of hexadecimal numbers.
        target_product (int): The target product.

    Returns:
        list: A list of pairs of hexadecimal numbers that, when multiplied, result in the target product.
    """

    # Initialize an empty list to store the result
    result = []

    # Convert the target product to an integer for comparison
    target_product = int(target_product, 16)

    # Iterate over the list of hexadecimal numbers
    for i in range(len(hex_list)):
        # Convert the current hexadecimal number to an integer
        num1 = int(hex_list[i], 16)
        
        # Iterate over the remaining hexadecimal numbers in the list
        for j in range(i + 1, len(hex_list)):
            # Convert the current hexadecimal number to an integer
            num2 = int(hex_list[j], 16)
            
            # Check if the product of the two numbers equals the target product
            if num1 * num2 == target_product:
                # If it does, add the pair to the result list
                result.append((hex_list[i], hex_list[j]))

    # Return the result list
    return result