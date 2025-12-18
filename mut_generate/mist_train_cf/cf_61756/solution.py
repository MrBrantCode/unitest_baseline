"""
QUESTION:
Create a function `rounded_avg_custom_base(n, m, base)` that takes three parameters: two positive integers `n` and `m` where `n <= m`, and an integer `base` within the interval [2, 10]. The function calculates the divisor-weighted average of the sequential integers from `n` to `m` (inclusive), rounds it to the nearest integer, and converts the result to the specified base. If `n > m` or `base` is outside the permitted range, the function returns -1.
"""

def rounded_avg_custom_base(n, m, base):
    """
    Calculate the divisor-weighted average of the sequential integers from n to m (inclusive),
    round it to the nearest integer, and convert the result to the specified base.

    Args:
        n (int): The start of the sequence (inclusive).
        m (int): The end of the sequence (inclusive).
        base (int): The base to convert the result to.

    Returns:
        str: The result as a string in the specified base, or -1 if the inputs are invalid.
    """
    if not 1 <= n <= m or not 2 <= base <= 10:
        return -1
    total, count = 0, 0
    for i in range(n, m+1):  
        total += i  
        count += 1  
    avg = round(total / count)  
    if base == 2:  
        return bin(avg)[2:]  # Remove '0b' prefix
    elif base == 8:  
        return oct(avg)[2:]  # Remove '0o' prefix
    elif base == 10:  
        return str(avg)
    else:  
        return to_base_x(avg, base)

def to_base_x(n, base):
    """
    Convert an integer to a custom base.

    Args:
        n (int): The number to convert.
        base (int): The base to convert to.

    Returns:
        str: The number in the specified base.
    """
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_base_x(n // base, base) + convert_string[n % base]