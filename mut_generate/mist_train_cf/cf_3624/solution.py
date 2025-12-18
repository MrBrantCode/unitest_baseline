"""
QUESTION:
Create a function `fibonacci_sequence(n)` that prints a Fibonacci sequence up to the nth term and returns the sum of all the numbers in the sequence. The function should not use recursion or any built-in functions related to the Fibonacci sequence, and the input `n` should be a positive integer greater than or equal to 3. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def fibonacci_sequence(n):
    if n < 3:
        return "n should be greater than or equal to 3"
    
    # Initialize the first two terms
    term1, term2 = 0, 1
    fibonacci_sum = term1 + term2
    
    # Print the first two terms
    print(term1)
    print(term2)
    
    # Generate the remaining terms and calculate the sum
    for i in range(3, n+1):
        current_term = term1 + term2
        fibonacci_sum += current_term
        print(current_term)
        
        # Update the values for the next iteration
        term1, term2 = term2, current_term
    
    return fibonacci_sum