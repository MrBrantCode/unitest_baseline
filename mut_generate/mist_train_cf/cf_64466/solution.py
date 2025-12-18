"""
QUESTION:
Find a contiguous subarray of hexadecimal numbers within a given chain that, when multiplied together, yields a specific target product. Implement a function named `find_subarray` that takes a list of hexadecimal strings and a target product as input, and returns the subarray of hexadecimal numbers that multiplies to the target product.
"""

def find_subarray(hex_array, target_product):
    """
    Find a contiguous subarray of hexadecimal numbers within a given chain 
    that, when multiplied together, yields a specific target product.

    Args:
        hex_array (list): A list of hexadecimal strings.
        target_product (int): The target product.

    Returns:
        list: The subarray of hexadecimal numbers that multiplies to the target product.
    """
    # Convert hexadecimal strings to integers and store them in a new list
    decimal_array = [int(hex_num, 16) for hex_num in hex_array]
    
    # Initialize variables to keep track of the current product and the start index of the subarray
    current_product = 1
    start = 0
    
    # Initialize a variable to store the subarray that multiplies to the target product
    result = []
    
    # Iterate over the decimal array
    for end, num in enumerate(decimal_array):
        # Update the current product
        current_product *= num
        
        # While the current product is greater than the target product, 
        # divide the current product by the number at the start index and increment the start index
        while current_product > target_product and start <= end:
            current_product //= decimal_array[start]
            start += 1
        
        # If the current product equals the target product, update the result
        if current_product == target_product:
            result = hex_array[start:end + 1]
    
    return result