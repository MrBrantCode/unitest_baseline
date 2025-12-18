"""
QUESTION:
Write a function `generate_fibonacci_series(n)` that generates the Fibonacci series up to the given number `n` using recursion. The function should have a time complexity of O(n) and a space complexity of O(1), excluding the space used for the output. Handle edge cases where the input number is 0 or 1, returning an empty list for `n = 0` and a list containing only 0 for `n = 1`.
"""

def generate_fibonacci_series(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    fibonacci_series = [0, 1]
    def generate_fibonacci_helper(n, fibonacci_series):
        current_number = fibonacci_series[-1]
        previous_number = fibonacci_series[-2]
        next_number = current_number + previous_number
        
        if next_number > n:
            return
        
        fibonacci_series.append(next_number)
        generate_fibonacci_helper(n, fibonacci_series)
    
    generate_fibonacci_helper(n, fibonacci_series)
    return fibonacci_series