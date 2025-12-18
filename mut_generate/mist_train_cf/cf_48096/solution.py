"""
QUESTION:
Construct the function `tetra(n)` to generate the distinct Tetranacci sequence. The sequence is defined by the following rules: 
- tetra(1) equals 4, 
- For even-indexed terms, tetra(n) is computed as the sum of 1 and n halved, 
- Terms that are divisible by 3 have tetra(n) equal to the total of the precedent term and the one before it, 
- For the remaining odd-indexed terms, tetra(n) quantifies to the total of the immediate previous term, the term preceding it, and the term three positions past. 
Given a non-negative integer input n, the function should output a list of the first n + 1 components from the Tetranacci sequence.
"""

def tetra(n):
    # Initialize list with initial tetranacci numbers
    tetra_sequence = [0, 4, 2, 6, 3] 
    for i in range(5, n+1):
        if i % 2 == 0: #even-indexed term
            tetra_sequence.append(1 + i // 2) 
        elif i % 3 == 0: #term divisible by 3
            tetra_sequence.append(tetra_sequence[i-1] + tetra_sequence[i-2]) 
        else: #remaining odd-index terms
            tetra_sequence.append(tetra_sequence[i-1] + tetra_sequence[i-2] + tetra_sequence[i-3]) 
    return tetra_sequence[1:n+1] #return required sequence