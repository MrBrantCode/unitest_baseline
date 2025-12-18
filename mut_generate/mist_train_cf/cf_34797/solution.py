"""
QUESTION:
Write a function `dailyTemperatures(T)` that takes a list of daily temperatures as input and returns a new list representing the number of days until a warmer temperature. If there is no future day with a warmer temperature, put 0 instead. The function should return the result list efficiently.
"""

def dailyTemperatures(T):
    stack = []
    result = [0] * len(T)

    for i in range(len(T) - 1, -1, -1):
        while stack and T[stack[-1]] <= T[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1] - i
        stack.append(i)

    return result