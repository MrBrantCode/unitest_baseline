"""
QUESTION:
Write a function `compare_and_check_numbers` that takes two integers as input, compares them, and prints the larger one. If the numbers are equal, it should print a message stating that the numbers are equal. Additionally, it should print a message stating whether the larger number is a prime number or not. The function should also check if the larger number is divisible by both 3 and 5, and print a message stating whether it is divisible by both, divisible by only one, or not divisible by either. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def compare_and_check_numbers(a, b):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_divisibility(n):
        if n % 3 == 0 and n % 5 == 0:
            return "divisible by both"
        elif n % 3 == 0:
            return "divisible by only 3"
        elif n % 5 == 0:
            return "divisible by only 5"
        else:
            return "not divisible by either"

    if a == b:
        print("The numbers are equal.")
    else:
        if a > b:
            larger = a
        else:
            larger = b

        print("The larger number is:", larger)

        if is_prime(larger):
            print("The larger number is a prime number.")
        else:
            print("The larger number is not a prime number.")

        print("Divisibility check:", check_divisibility(larger))