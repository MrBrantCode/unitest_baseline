"""
QUESTION:
Write a function `sumEvenNumbers` that takes a list of integers as input and returns the sum of all the even numbers in the list. The function should only use the following characters: `(`, `)`, `{`, `}`, `[`, `]`, `<`, `>`, `+`, `-`, `*`, `/`, `%`, `!`, `=`, `;`, `:`, `|`, `&`, `^`, `~`, `0-9`, `a-z`, and `A-Z`.
"""

def sumEvenNumbers(arr):
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total