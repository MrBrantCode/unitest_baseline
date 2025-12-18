"""
QUESTION:
Create a function called `tetra` that takes a non-negative integer `n` and returns a list of the first `n + 1` numbers of the Tetranacci sequence. The Tetranacci sequence is defined by the following rules: 
- The first term `tetra(1)` is 4, 
- For even terms, `tetra(n)` is calculated as `(n + 1) / 2`, 
- For terms divisible by 3, `tetra(n)` is the sum of the two preceding terms, 
- For odd terms not divisible by 3, `tetra(n)` is the sum of the three preceding terms.
"""

def tetra(n):
    if n<1:
        return []
    sequence = [1,4]
    for num in range(2, n+1): # Finding the tetra values for each num until n
        if num % 2 == 0:
            value = 1 + num // 2
        elif num % 3 == 0:
            value = sequence[-1] + sequence[-2]
        else:
            value = sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(value) # Appending it in the list
    return sequence[:n+1] # N+1 values