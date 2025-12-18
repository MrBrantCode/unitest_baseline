"""
QUESTION:
Create a function `rev_fib(n)` that generates Fibonacci numbers up to 'n' in reverse order. The function should handle negative numbers and non-integer inputs. The Fibonacci sequence should start from 1 (i.e., 1, 1, 2, 3, 5, ...). The function should be optimized for a reduced time complexity.
"""

def rev_fib(n):
    try:
        n = int(n)
        if n < 1:
            print("Not a positive integer!")
            return
    except ValueError:
        print("Not an integer!")
        return

    result = [1, 1]
    for _ in range(2, n):
        result.append(result[-1] + result[-2])
    return result[::-1]  # Use list slicing to obtain the reverse order.