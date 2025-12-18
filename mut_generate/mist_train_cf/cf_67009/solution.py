"""
QUESTION:
Implement a function named `ema` that calculates the Exponential Moving Average (EMA) of a given list of numbers using the formula EMA[i] = (close[i]-EMA[i-1])*lambda + EMA[i-1], where lambda = 2/(i+1). Note that this implementation should start from the second element in the list (i.e., 1 <= i < len) and the function should return the list of calculated EMA values.
"""

def ema(numbers):
    if len(numbers) == 0:
        return []
    
    ema_values = [numbers[0]]
    for i in range(1, len(numbers)):
        lambda_val = 2/(i+1)
        ema_values.append((numbers[i]-ema_values[i-1])*lambda_val + ema_values[i-1])
    return ema_values[1:]