"""
QUESTION:
Write a function `tri(n)` that generates a sequence of integers based on the given integer `n`. The sequence should be generated according to the following rules:
- If `n` is less than 0, return an empty sequence.
- If `n` is 0 or more, append 3 to the sequence.
- If `n` is 2 or more, append 2 to the sequence.
- If `n` is 3 or more, append the sum of the last two numbers in the sequence plus 1.
- For `n` greater than 3, iterate from 4 to `n` and append numbers to the sequence according to the following rules:
  - If the current number is even, append the number divided by 2 plus 1.
  - If the current number is odd, append the sum of the last three numbers in the sequence.

The function should return the generated sequence.
"""

def tri(n):
    sequence = []
    if n < 0:
        return sequence
    if n >= 0:
        sequence.append(3)
    if n >= 2:
        sequence.append(2)
    if n >= 3:
        sequence.append(sequence[-2] + sequence[-1] + 1)
    for i in range(4, n+1):
        if i%2==0:
            sequence.append(1 + i // 2)
        else:
            sequence.append(sequence[-2] + sequence[-1] + sequence[-3])
    return sequence