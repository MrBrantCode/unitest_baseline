"""
QUESTION:
Create a function named `dailyTemperatures` that takes a sequence of daily temperatures `T` as input. The function should return a list where each element at index `i` represents the number of days until a warmer temperature is recorded. If no warmer temperature is recorded, the value should be `0`. The input list `T` will contain between `1` and `30,000` elements, with each temperature being a whole number within the range `[30, 100]`.
"""

def dailyTemperatures(T):
    res = [0] * len(T)
    stack = []
    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res