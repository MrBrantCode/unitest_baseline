"""
QUESTION:
Find a subset of hexadecimal numbers within a list that when multiplied together equal a predetermined result.
"""

def find_hex_subset(hex_numbers, target_result):
    """
    Find a subset of hexadecimal numbers in a list that when multiplied together equal a target result.

    Args:
        hex_numbers (list): A list of hexadecimal numbers.
        target_result (int): The predetermined result.

    Returns:
        list: A subset of hexadecimal numbers that multiply to the target result. If no subset is found, returns an empty list.
    """

    def backtrack(start, path, product):
        if product == target_result:
            result.append(path)
            return
        if product > target_result:
            return
        for i in range(start, len(hex_numbers)):
            # Convert hexadecimal to integer for multiplication
            num = int(hex_numbers[i], 16)
            backtrack(i + 1, path + [hex_numbers[i]], product * num)

    result = []
    backtrack(0, [], 1)
    return result