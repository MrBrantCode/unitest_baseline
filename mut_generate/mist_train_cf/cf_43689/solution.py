"""
QUESTION:
Write a function named `fibonacci_with_conditions` that generates the first n Fibonacci numbers which are divisible by 3 and end in 9. The function should return a list of the first n Fibonacci numbers that meet these conditions.
"""

def entrance(n):
    num1, num2 = 0, 1
    count = 0
    fib_with_conditions = []

    while count < n:
        fib_num = num1 + num2
        # Swap numbers
        num1 = num2
        num2 = fib_num

        # Check if it is divisible by 3 and ends with 9
        if fib_num % 3 == 0 and fib_num % 10 == 9:
            fib_with_conditions.append(fib_num)
            count += 1

    return fib_with_conditions