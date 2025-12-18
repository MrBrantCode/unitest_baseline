"""
QUESTION:
Create a function named rounded_avg_custom_base that takes three parameters: n, m, and base. n and m are positive integers where n is less than or equal to m, and base is an integer between 2 and 10 (inclusive) representing the desired custom base system for the result. The function should return a string representing the weighted average of the integers from n through m (including n and m), with weights given by their divisors' count, rounded to the nearest integer and converted to the specified custom base. If n is greater than m or base is outside of the allowed range, return -1.
"""

def rounded_avg_custom_base(n: int, m: int, base: int) -> str:
    """
    Calculate the weighted average of the integers from n through m (including n and m), 
    with weights given by their divisors' count, rounded to the nearest integer and 
    converted to the specified custom base.

    Args:
    n (int): A positive integer representing the starting number in a range (n <= m).
    m (int): A positive integer representing the ending number in a range.
    base (int): An integer between 2 and 10 (inclusive) representing the desired custom base system for the result.

    Returns:
    str: A string representation of the weighted average in the specified custom base, or -1 if the input is invalid.
    """

    # Check if n is greater than m or base is outside of the allowed range
    if n > m or not 2 <= base <= 10:
        return -1

    def count_divisors(num: int) -> int:
        """
        Helper function to compute the divisors' count of a given number.

        Args:
        num (int): A positive integer.

        Returns:
        int: The count of divisors of num.
        """
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return count

    total_weight = 0
    total_sum = 0
    for i in range(n, m + 1):
        weight = count_divisors(i)
        total_weight += weight
        total_sum += i * weight

    weighted_avg = total_sum / total_weight
    rounded_avg = round(weighted_avg)

    # Convert the rounded average to the custom base representation
    if base == 2:
        custom_base = "0b" + bin(rounded_avg)[2:]
    elif base == 8:
        custom_base = "0o" + oct(rounded_avg)[2:]
    else:
        custom_base = ""
        while rounded_avg > 0:
            remainder = rounded_avg % base
            custom_base = str(remainder) + custom_base
            rounded_avg //= base
        custom_base = str(base) + custom_base

    return custom_base