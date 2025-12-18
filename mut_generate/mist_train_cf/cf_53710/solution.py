"""
QUESTION:
Write a function `hex_pairs_product` that takes a list of hexadecimal numbers and a target product as input. The function should return a list of pairs of hexadecimal numbers from the input list that multiply to the target product. The function should work with hexadecimal numbers represented as strings.
"""

def hex_pairs_product(hex_list, target_product):
    """
    This function takes a list of hexadecimal numbers and a target product as input.
    It returns a list of pairs of hexadecimal numbers from the input list that multiply to the target product.

    Parameters:
    hex_list (list): A list of hexadecimal numbers as strings.
    target_product (int): The target product.

    Returns:
    list: A list of pairs of hexadecimal numbers that multiply to the target product.
    """
    
    # Convert target product to integer
    target_product = int(target_product, 16)
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the list of hexadecimal numbers
    for i in range(len(hex_list)):
        # Convert the current hexadecimal number to integer
        num1 = int(hex_list[i], 16)
        
        # Iterate over the rest of the list
        for j in range(i + 1, len(hex_list)):
            # Convert the current hexadecimal number to integer
            num2 = int(hex_list[j], 16)
            
            # Check if the product of the two numbers equals the target product
            if num1 * num2 == target_product:
                # If it does, add the pair to the result list
                result.append((hex_list[i], hex_list[j]))
    
    # Return the result list
    return result