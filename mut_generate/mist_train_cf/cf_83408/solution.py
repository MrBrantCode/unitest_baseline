"""
QUESTION:
Write a function named `find_hex_sequence` that takes two parameters: an array of hexadecimal digits and a target product. The function should return the longest contiguous subsequence of hexadecimal digits that, when multiplied together, equal the target product.
"""

def find_hex_sequence(hex_digits, target_product):
    """
    Find the longest contiguous subsequence of hexadecimal digits that, when multiplied together, equal the target product.

    Args:
        hex_digits (list): A list of hexadecimal digits.
        target_product (int): The target product.

    Returns:
        list: The longest contiguous subsequence of hexadecimal digits.
    """
    max_length = 0
    result = []
    left = 0
    product = 1

    for right in range(len(hex_digits)):
        product *= int(hex_digits[right], 16)
        
        while product >= target_product and left <= right:
            if product == target_product and right - left + 1 > max_length:
                max_length = right - left + 1
                result = hex_digits[left:right + 1]
            product //= int(hex_digits[left], 16)
            left += 1

    return result