"""
QUESTION:
Write a function named `print_message` that takes two parameters: a boolean `condition` and an integer `specific_variable`. The function should print a message only if `condition` is true and `specific_variable` is greater than 5, an odd number, and a prime number.
"""

def print_message(condition, specific_variable):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if condition and specific_variable > 5 and specific_variable % 2 != 0 and is_prime(specific_variable):
        print("The condition is true and the specific variable is greater than 5, odd, and prime.")
    elif condition:
        print("The condition is true, but the specific variable does not meet the requirements.")