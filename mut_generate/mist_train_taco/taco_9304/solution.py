"""
QUESTION:
We have a sequence of N integers: x=(x_0,x_1,\cdots,x_{N-1}). Initially, x_i=0 for each i (0 \leq i \leq N-1).

Snuke will perform the following operation exactly M times:

* Choose two distinct indices i, j (0 \leq i,j \leq N-1,\ i \neq j). Then, replace x_i with x_i+2 and x_j with x_j+1.



Find the number of different sequences that can result after M operations. Since it can be enormous, compute the count modulo 998244353.

Constraints

* 2 \leq N \leq 10^6
* 1 \leq M \leq 5 \times 10^5
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N M


Output

Print the number of different sequences that can result after M operations, modulo 998244353.

Examples

Input

2 2


Output

3


Input

3 2


Output

19


Input

10 10


Output

211428932


Input

100000 50000


Output

3463133
"""

def count_different_sequences(N, M):
    """
    Calculate the number of different sequences that can result after performing M operations on a sequence of N integers.

    Parameters:
    N (int): The number of integers in the sequence.
    M (int): The number of operations to perform.

    Returns:
    int: The number of different sequences modulo 998244353.
    """
    (w, u) = (3 * M, N - 1)
    (o, f, i) = (998244353, [1], 1)
    
    # Calculate factorials up to w + n
    while i < w + N:
        f.append(f[-1] * i % o)
        i += 1
    
    # Helper function to calculate combinations
    c = lambda n, k=u: f[n] * pow(f[n - k], o - 2, o) * pow(f[k], o - 2, o) % o
    
    # Calculate the result
    a = c(w + u) - N * c(N + M - 2)
    while ~-N > M < w:
        M += 2
        a -= c(N, M) * c(2 * u + w - M >> 1)
    
    return a % o