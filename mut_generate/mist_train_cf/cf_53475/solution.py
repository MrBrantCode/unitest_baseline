"""
QUESTION:
Write a function `find_hex_cluster` that identifies a cluster of hexadecimal numerals within a series where the product of the cluster's elements equals a predetermined result.
"""

def find_hex_cluster(hex_series, target_product):
    """
    Finds a cluster of hexadecimal numerals within a series where the product of the cluster's elements equals a predetermined result.

    Args:
    hex_series (list): A list of hexadecimal numbers.
    target_product (int): The target product of the cluster's elements.

    Returns:
    list: A cluster of hexadecimal numerals where the product of the cluster's elements equals the target product. If no such cluster is found, returns an empty list.
    """
    def backtrack(start, path, product):
        if product == target_product:
            return path
        if product > target_product or start >= len(hex_series):
            return []
        # Try including the current number in the product
        included = backtrack(start + 1, path + [hex_series[start]], product * int(hex_series[start], 16))
        if included:
            return included
        # Try excluding the current number from the product
        return backtrack(start + 1, path, product)

    return backtrack(0, [], 1)