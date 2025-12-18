"""
QUESTION:
Find a specific group of hexadecimal numbers in a series that, when multiplied together, equal a given number. The function, `find_hex_cluster`, should take a list of hexadecimal numbers and a target product as input and return the group of hexadecimal numbers that multiply to the target product.
"""

def find_hex_cluster(hex_list, target_product):
    """
    Finds a group of hexadecimal numbers in a series that, when multiplied together, equal a given number.

    Args:
    hex_list (list): A list of hexadecimal numbers.
    target_product (int): The target product.

    Returns:
    list: The group of hexadecimal numbers that multiply to the target product.
    """
    def backtrack(start, path, product):
        if product == target_product:
            result.append(path)
            return
        if product > target_product:
            return
        for i in range(start, len(hex_list)):
            new_product = product * int(hex_list[i], 16)
            if new_product <= target_product:
                backtrack(i + 1, path + [hex_list[i]], new_product)

    result = []
    backtrack(0, [], 1)
    return result