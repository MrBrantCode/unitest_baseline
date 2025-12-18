"""
QUESTION:
Write a function `myfunc(n)` that calculates the total number of iterations where all four indices `i`, `j`, `k`, and `l` are even, given four nested loops each iterating `n` times.
"""

def myfunc(n):
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and l % 2 == 0:
                        count += 1
    return count