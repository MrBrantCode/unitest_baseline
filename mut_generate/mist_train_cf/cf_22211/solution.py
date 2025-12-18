"""
QUESTION:
Write a function named `filter_prime_numbers` that takes a list of integers as input, filters out the prime numbers, and returns the filtered list. The function should handle errors, including non-integer values in the input list, and provide appropriate error messages.
"""

def filter_prime_numbers(numbers):
    """
    Filter out prime numbers from a list of integers
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    try:
        prime_numbers = [num for num in numbers if is_prime(num)]
        return prime_numbers
    except TypeError:
        print("Error: The input list must contain only integers")
        return []
    except Exception as e:
        print("An error occurred during filtering:", str(e))
        return []