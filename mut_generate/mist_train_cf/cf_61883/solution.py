"""
QUESTION:
Create a function named `list_factorial` that calculates the factorial of numbers in a list. The function should handle non-integer and negative integer inputs by skipping them and printing a corresponding message. The function should return a dictionary where the keys are the input numbers and the values are their corresponding factorials. The factorial calculation should be based on the mathematical definition: n! = n * (n-1)!. The input list can contain any type of elements.
"""

def list_factorial(lst):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)

    factorials = {}
    for i in lst:
        if type(i) == int:
            if i >= 0:
                factorials[i] = factorial(i)
            else:
                print(f"Negative number {i} ignored. Factorial not defined for negative numbers.")
        else:
            print(f"Non-integer {i} ignored. Factorial only defined for non-negative integers.")
    return factorials