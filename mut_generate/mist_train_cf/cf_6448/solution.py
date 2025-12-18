"""
QUESTION:
Write a Python program with two functions: `sum_powers_of_2(n)` and `product_powers_of_3(n)`. The function `sum_powers_of_2(n)` should recursively calculate the sum of all powers of 2 up to 2^n. The function `product_powers_of_3(n)` should use a nested loop to calculate the product of all powers of 3 up to 3^n. The program should then take an integer `n` as input and print out the sum of all powers of 2 and the product of all powers of 3 up to the given power `n`.
"""

def entrance(n):
    def sum_powers_of_2(n):
        if n == 0:
            return 1
        else:
            return 2 ** n + sum_powers_of_2(n-1)

    def product_powers_of_3(n):
        product = 1
        for i in range(n+1):
            product *= 3 ** i
        return product

    print("Sum of powers of 2:", sum_powers_of_2(n))
    print("Product of powers of 3:", product_powers_of_3(n))

# n = int(input("Enter the value of n: "))
# entrance(n)