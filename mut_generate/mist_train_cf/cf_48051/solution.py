"""
QUESTION:
Create a function `find_fibonacci_elements(input_list, k)` that takes an integer list and an integer `k` as input. The function should iterate through the list to find the kth Fibonacci number and count the total number of Fibonacci numbers in the list. The function should return a tuple containing the total count of Fibonacci numbers and the kth Fibonacci number. The function should run in O(n) time complexity, where n is the size of the input list.
"""

def is_fibonacci(n):
    if n<0:
        return False
    x = (5*n*n + 4)
    y = (5*n*n - 4)
    return x**0.5 % 1 == 0 or y**0.5 % 1 == 0

def find_fibonacci_elements(input_list, k):
    count_fib = 0
    kth_fib = None

    for elem in input_list:
        if is_fibonacci(elem):
            count_fib += 1
            if count_fib == k:
                kth_fib = elem

    return count_fib, kth_fib