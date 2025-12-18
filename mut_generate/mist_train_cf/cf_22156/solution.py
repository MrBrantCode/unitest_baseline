"""
QUESTION:
Write a function `sequence(n)` that returns the nth number in a sequence where each number is formed by reading the previous number digit by digit, counting the number of consecutive occurrences of each digit, and concatenating the count followed by the digit itself. The function should take an integer `n` as input and return the corresponding sequence number as a string.

The input `n` is restricted to the range 1 ≤ n ≤ 50.
"""

def sequence(n):
    if n == 1:
        return "1"
    else:
        prev = sequence(n-1)
        count = 1
        result = ""
        for i in range(1, len(prev)):
            if prev[i] == prev[i-1]:
                count += 1
            else:
                result += str(count) + prev[i-1]
                count = 1
        result += str(count) + prev[-1]
        return result