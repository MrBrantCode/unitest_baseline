"""
QUESTION:
Write a program that takes two integers as input, `num1` and `num2`, where 1 ≤ `num1` and `num2` ≤ 100. The program should calculate and print the multiplication of `num1` and `num2`, check if both numbers are prime, and print a message indicating whether they are prime or not. Additionally, the program should check if the multiplication is divisible by 5 and print the corresponding message. The program should also calculate and print the sum of all prime numbers between `num1` and `num2` (inclusive).
"""

def entrance(num1, num2):
    """
    This function takes two integers as input, num1 and num2, 
    calculates and prints the multiplication of num1 and num2, 
    checks if both numbers are prime, and prints a message indicating 
    whether they are prime or not. It also checks if the multiplication 
    is divisible by 5 and prints the corresponding message. 
    Additionally, it calculates and prints the sum of all prime numbers 
    between num1 and num2 (inclusive).
    """
    
    def is_prime(num):
        """
        Helper function to check if a number is prime.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_primes(num1, num2):
        """
        Helper function to calculate the sum of all prime numbers 
        between num1 and num2 (inclusive).
        """
        primes = []
        for num in range(num1, num2 + 1):
            if is_prime(num):
                primes.append(num)
        return sum(primes)

    multiplication = num1 * num2
    print("The multiplication of the two numbers is:", multiplication)

    if is_prime(num1) and is_prime(num2):
        print("The numbers are prime.")
    else:
        print("The numbers are not prime.")

    if multiplication % 5 == 0:
        print("The multiplication is divisible by 5.")
    else:
        print("The multiplication is not divisible by 5.")

    sum_of_primes = sum_primes(num1, num2)
    print("The sum of all prime numbers between", num1, "and", num2, "is:", sum_of_primes)