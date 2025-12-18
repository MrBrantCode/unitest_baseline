"""
QUESTION:
Create a function to check if an integer is prime and another to calculate the factorial of an integer. Use these functions to loop through numbers from 1 to 20 (inclusive), check if each number is even or odd, and perform the following operations:
- For even numbers, calculate and print their factorial in the format "The factorial of <number> is <factorial>".
- For odd numbers, check if they are prime numbers. If they are prime, print "<number> is a prime number", otherwise just print the number. Use only loops and conditionals, without any built-in functions or libraries dedicated to these tasks.
"""

def entance(n):
    def check_prime(num):
        if num == 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:  
                    return False
            return True 

    def calculate_factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    for num in range(1, n+1):
        
        # Check if even
        if num % 2 == 0:
            # calculate the factorial
            fact = calculate_factorial(num)
            print(f"The factorial of {num} is {fact}")
        
        # Else it's odd
        else:
            # check if number is prime
            if check_prime(num):
                print(f"{num} is a prime number")
            else:
                print(num)