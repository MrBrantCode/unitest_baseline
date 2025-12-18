"""
QUESTION:
Create a function `num_classification` that takes a string of comma-separated integers as input, classifies each integer as even, odd, or zero, and returns the count of each. The function should handle invalid inputs (non-integer values) by printing an error message and exiting.
"""

def num_classification(input_str):
    """
    Classify each integer in a comma-separated string as even, odd, or zero and return the count of each.

    Args:
        input_str (str): A string of comma-separated integers.

    Returns:
        dict: A dictionary containing the count of even, odd, and zero numbers.
    """
    even_count = 0
    odd_count = 0
    zero_count = 0

    try:
        number_list = [int(i) for i in input_str.split(",")]
    except ValueError:
        print("Invalid input. Please only enter comma-separated integers.")
        return None

    for num in number_list:
        if num == 0:
            zero_count += 1
        elif num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return {"even": even_count, "odd": odd_count, "zero": zero_count}