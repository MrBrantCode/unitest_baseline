"""
QUESTION:
Create a function called `prime_sum` that calculates the sum of prime numbers between two given numbers `start` and `end` (inclusive), and also prints each prime number. The function should take two parameters `start` and `end`, where `start` is less than or equal to `end`. The function should not take any other parameters.
"""

def prime_sum(start, end):
    """
    Calculates the sum of prime numbers between two given numbers (inclusive) and prints each prime number.

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        int: The sum of prime numbers between start and end.
    """
    prime_sum = 0

    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)
                prime_sum += num

    print("Sum of prime numbers:", prime_sum)
    return prime_sum