"""
QUESTION:
Create a function called `fibonacci_word(n)` that takes an integer `n` as input and returns the corresponding term in the Fibonacci word sequence, where the sequence is defined by concatenating the (n-1)th term and the (n-2)th term for n > 2, with the base cases being the 1st term as "1" and the 2nd term as "0". The function should be efficient for large values of `n`.
"""

def fibonacci_word(n):
    fibonacci_word_sequence = ['1', '0']
    
    for i in range(2, n):
        fibonacci_word_sequence.append(fibonacci_word_sequence[i-1] + fibonacci_word_sequence[i-2])
    
    return fibonacci_word_sequence[n-1]