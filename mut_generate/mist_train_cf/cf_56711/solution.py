"""
QUESTION:
Write a function `multiplication_table(n)` that takes a number `n` as input and returns a tuple containing its multiplication table up to 10 and the sum of the generated multiplication table. The multiplication table should be a list of numbers from `n*1` to `n*10`. The function should return both the list and the sum of the elements in the list.
"""

def multiplication_table(n):
    results = [n*i for i in range(1, 11)]
    return (results, sum(results))