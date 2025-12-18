"""
QUESTION:
Let f(n) be the number of triples of integers (x,y,z) that satisfy both of the following conditions:

* 1 \leq x,y,z
* x^2 + y^2 + z^2 + xy + yz + zx = n



Given an integer N, find each of f(1),f(2),f(3),\ldots,f(N).

Constraints

* All values in input are integers.
* 1 \leq N \leq 10^4

Input

Input is given from Standard Input in the following format:


N


Output

Print N lines. The i-th line should contain the value f(i).

Example

Input

20


Output

0
0
0
0
0
1
0
0
0
0
3
0
0
0
0
0
3
3
0
0
"""

def count_valid_triples(N):
    """
    Counts the number of valid triples (x, y, z) that satisfy the equation:
    x^2 + y^2 + z^2 + xy + yz + zx = n
    for each n in the range from 1 to N.

    Parameters:
    N (int): The upper limit of the range for which to compute the counts.

    Returns:
    list: A list of integers where the i-th element represents f(i+1).
    """
    import math
    nn = int(math.sqrt(N)) + 1
    a = [0] * (100 * N)
    
    for x in range(1, nn + 1):
        for y in range(1, nn + 1):
            for z in range(1, nn + 1):
                index = (x + y + z) ** 2 - x * y - x * z - y * z
                if index <= N:
                    a[index] += 1
    
    return a[1:N+1]