"""
QUESTION:
Create a function `fib_word_seq(m, n)` to calculate the m-th Fibonacci word and its prefix and suffix sequences of lengths 1 to n. The function must take two integers m and n as arguments where m > 2 and n < m. It should return a dictionary with keys 'Fib_seq', 'Prefixes', and 'Suffixes' containing the m-th Fibonacci word, a list of n word prefixes, and a list of n word suffixes respectively. If m or n are non-positive, return 'Invalid Input'.
"""

def fib_word_seq(m, n):
    # Check for non-positive inputs
    if m <= 0 or n <= 0 or n >= m:
        return 'Invalid Input'

    # Initialize the first two Fibonacci words
    fib_words = ['0', '01']
    
    # Generate Fibonacci words until the m-th term
    for i in range(2, m):
        fib_words.append(fib_words[i - 1] + fib_words[i - 2])

    # Get the m-th Fibonacci word
    fib_word = fib_words[-1]

    # Get the prefix and suffix sequences
    prefixes = [fib_word[:i] for i in range(1, n + 1)]
    suffixes = [fib_word[-i:] for i in range(1, n + 1)]

    # Organize the results in a dictionary
    result = {'Fib_seq': fib_word, 'Prefixes': prefixes, 'Suffixes': suffixes}

    return result