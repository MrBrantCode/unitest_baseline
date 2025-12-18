"""
QUESTION:
Write a function named `check_pass` that takes an integer `n` as input, and outputs "pass" with a time complexity of O(n^2). The function should have a variable `sum` initialized to 0, and should increment this variable in a way that results in a total of `n * n` increments. The output should be "pass" if and only if the final value of `sum` is equal to `n * n`.
"""

def check_pass(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += 1
    return "pass" if sum == n * n else None