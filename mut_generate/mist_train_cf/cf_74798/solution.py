"""
QUESTION:
Write a function `hepta(n)` that generates a list of the first `n + 1` numbers from the Heptanacci sequence, where the sequence follows these rules:
- `hepta(1)` equals 7,
- for terms divisible by 2, `hepta(n)` equals the sum of 1 and `n` divided by 3,
- for terms divisible by 5, `hepta(n)` is the sum of the previous two terms and the term four steps back,
- for terms divisible by 3, `hepta(n)` is the sum of the previous three terms,
- for other odd terms, `hepta(n)` is the sum of the previous four terms.
The function should return a list of non-negative integers. Note that when `n` is 0, the function should return `[1]`.
"""

def hepta(n):
    if n == 0:
        return [1]
    hepta_sequence = [1, 7]
    for i in range(2,n+1):
        if i % 2 == 0:
            hepta_sequence.append(1 + i//3) 
        elif i % 5 == 0:
            hepta_sequence.append(hepta_sequence[i - 1] + hepta_sequence[i - 2] + hepta_sequence[i - 4])
        elif i % 3 == 0:
            hepta_sequence.append(hepta_sequence[i - 1] + hepta_sequence[i - 2] + hepta_sequence[i - 3])
        else:
            hepta_sequence.append(hepta_sequence[i - 1] + hepta_sequence[i - 2] + hepta_sequence[i - 3] + hepta_sequence[i - 4])
    return hepta_sequence