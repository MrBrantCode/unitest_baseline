"""
QUESTION:
Create a function `generatePattern(n)` that takes an integer `n` as input and returns a string consisting of `n` lines, where each line contains a sequence of numbers from 1 to the line number, separated by "+" signs. For example, `generatePattern(4)` should return the string "1\n1+2\n1+2+3\n1+2+3+4".
"""

def generatePattern(n):
    pattern = ""
    for i in range(1, n + 1):
        line = "+".join(str(j) for j in range(1, i + 1))
        pattern += line + "\n"
    return pattern.strip()