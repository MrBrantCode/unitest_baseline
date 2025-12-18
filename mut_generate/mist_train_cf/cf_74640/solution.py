"""
QUESTION:
Create a function named `binary_fibonacci` that takes a list of integers (ranging from 0 to 1000) as input and returns a list of Fibonacci numbers from the input list, represented in binary format. The function should use a list comprehension.
"""

def binary_fibonacci(input_list):
    def fibonacci_series(limit):
        num1, num2 = 0, 1
        fibo_list = [0]
        while num2 <= limit:
            fibo_list.append(num2)
            num1, num2 = num2, num1 + num2
        return fibo_list

    fibo_list = fibonacci_series(1000)
    return [bin(i)[2:] for i in input_list if i in fibo_list]