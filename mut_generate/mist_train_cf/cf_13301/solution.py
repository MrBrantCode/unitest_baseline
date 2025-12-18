"""
QUESTION:
Write a function named `print_odd_numbers` that takes a range defined by two integers `start` and `end` as input. The function should print all odd numbers in the range that are not divisible by 3. For each printed odd number, it should also check if the number is prime and print "Prime" next to it if it is. The function should return the sum of all printed odd numbers.
"""

def print_odd_numbers(start, end):
    """
    Prints all odd numbers in the range that are not divisible by 3.
    For each printed odd number, it checks if the number is prime and prints "Prime" next to it.
    Returns the sum of all printed odd numbers.

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        int: The sum of all printed odd numbers.
    """
    sum_of_odd_numbers = 0

    for num in range(start, end + 1):
        if num % 2 != 0:  # Check if the number is odd
            if num % 3 == 0:  # Check if the number is divisible by 3
                continue  # Skip to the next iteration if divisible by 3
            else:
                is_prime = True
                for i in range(2, int(num/2) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(num, "Prime")
                else:
                    print(num)
                sum_of_odd_numbers += num

    return sum_of_odd_numbers