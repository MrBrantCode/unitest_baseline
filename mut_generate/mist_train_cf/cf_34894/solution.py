"""
QUESTION:
Write a function `final_fibonacci_number` that takes a string `surname` as input and returns the sum of the Fibonacci numbers corresponding to the positions of the first and last letters of the surname in the English alphabet (a=1, b=2, ..., z=26), where the positions are case-insensitive and the Fibonacci sequence starts with 0 and 1. The function should handle surnames with one or more characters.
"""

def final_fibonacci_number(surname):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    first_letter_position = ord(surname[0].lower()) - 96  
    last_letter_position = ord(surname[-1].lower()) - 96  
    first_fibonacci = fibonacci(first_letter_position)  
    last_fibonacci = fibonacci(last_letter_position)  
    final_fibonacci = first_fibonacci + last_fibonacci  
    return final_fibonacci