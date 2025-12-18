"""
QUESTION:
Implement a function called `count_numbers` that takes a sequence of space-separated integers as input and returns a dictionary with the counts of positive even, positive odd, zero, negative even, and negative odd numbers. The function should handle exceptions that may occur due to non-integer inputs.
"""

def count_numbers(input_str):
    """
    This function takes a sequence of space-separated integers as input, 
    and returns a dictionary with the counts of positive even, positive odd, zero, negative even, and negative odd numbers.

    Args:
        input_str (str): A sequence of space-separated integers.

    Returns:
        dict: A dictionary with the counts of positive even, positive odd, zero, negative even, and negative odd numbers.
    """

    count_dict = {"positive_even": 0, "positive_odd": 0, "zero": 0, "negative_even": 0, "negative_odd": 0}

    def convert_to_int(string):
        try:
            return int(string)
        except ValueError:
            return None

    numbers = [num for num in map(convert_to_int, input_str.split()) if num is not None]

    for num in numbers:
        if num % 2 == 0:
            if num == 0:
                count_dict["zero"] += 1
            elif num > 0:
                count_dict["positive_even"] += 1
            else:
                count_dict["negative_even"] += 1
        else:
            if num > 0:
                count_dict["positive_odd"] += 1
            else:
                count_dict["negative_odd"] += 1

    return count_dict