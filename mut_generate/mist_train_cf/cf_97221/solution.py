"""
QUESTION:
Write a function `powers_of_two(n)` that prints all powers of 2 less than or equal to `n`, along with their binary representations and the sum of their binary digits. The function should also return or print the total sum of all binary digits. The input `n` is an integer and the function should handle all possible integer inputs.
"""

def powers_of_two(n):
    """
    Prints all powers of 2 less than or equal to `n`, along with their binary representations and the sum of their binary digits.
    Returns the total sum of all binary digits.

    Args:
        n (int): The upper limit for powers of 2.

    Returns:
        int: The total sum of all binary digits.
    """
    total_sum = 0

    for i in range(n):
        if 2 ** i <= n:
            binary_rep = bin(2 ** i)[2:]
            binary_sum = sum(int(digit) for digit in binary_rep)
            total_sum += binary_sum

            print(f"{2 ** i}: {binary_rep} ({'+'.join(list(binary_rep))} = {binary_sum})")

    print(f"Total sum of binary digits: {total_sum}")
    return total_sum