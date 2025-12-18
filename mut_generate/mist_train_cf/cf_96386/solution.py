"""
QUESTION:
Construct a function `print_fibonacci` that prints the Fibonacci numbers up to the nth term. The function should take one argument, `n`, representing the number of Fibonacci terms to print. Each number should be printed on a separate line.
"""

def print_fibonacci(n):
    """
    Prints the Fibonacci numbers up to the nth term.
    
    Args:
    n (int): The number of Fibonacci terms to print.
    """
    
    # Handle edge cases where n is less than or equal to 0
    if n <= 0:
        return
    
    # Initialize the first two terms of the Fibonacci sequence
    prev_num = 0
    curr_num = 1

    # Print the first term
    print(prev_num)
    
    # If n is 1, return after printing the first term
    if n == 1:
        return

    # Print the second term
    print(curr_num)
    
    # Loop to generate and print the Fibonacci numbers up to the nth term
    for _ in range(n - 2):  # We already printed the first two terms, so loop n-2 times
        next_num = prev_num + curr_num  # Calculate the next Fibonacci number
        print(next_num)  # Print the next Fibonacci number
        prev_num, curr_num = curr_num, next_num  # Update the previous and current numbers