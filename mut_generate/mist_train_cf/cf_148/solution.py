"""
QUESTION:
Create a function `compare_and_analyze` that takes two integers as input. The function should print the larger of the two integers and a message stating whether the larger number is a prime number or not. If the two numbers are equal, it should print a message stating that the numbers are equal. Additionally, it should print a message stating whether the larger number is divisible by both 3 and 5, divisible by only one, or divisible by neither. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def compare_and_analyze(a, b):
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
        larger = max(a, b)
        print("The larger number is:", larger)

        if is_prime(larger):
            print("The larger number is a prime number.")
        else:
            print("The larger number is not a prime number.")

        print("Divisibility check:", check_divisibility(larger))