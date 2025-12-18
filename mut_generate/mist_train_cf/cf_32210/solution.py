"""
QUESTION:
Create a function `daily_temperatures` that takes a list of integers representing daily temperatures as input and returns a list of integers representing the number of days to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
"""

def daily_temperatures(T):
    stack = []
    result = [0] * len(T)
    
    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    
    return result