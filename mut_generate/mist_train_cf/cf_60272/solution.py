"""
QUESTION:
Analyze the time and space complexity of `prodFunc(n)` and `advancedFunc(m)`. 

`prodFunc(n)` calculates the product of all positive integers up to `n` and `advancedFunc(m)` calculates the sum of factorials for all positive numbers up to `m` by calling `prodFunc(j)` for each `j` from 1 to `m`. Determine the time and space complexities of both functions and how the interdependency between them affects their complexities. Assume that `n` and `m` are positive integers greater than or equal to 1 and 2, respectively.
"""

def prodFunc(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def advancedFunc(m):
    total_sum = 0
    for j in range(1, m + 1):
        total_sum += prodFunc(j)
    return total_sum