"""
QUESTION:
Create a function called `create_chaos_indicators` that generates a tuple of chaotic indicators using the logistic map algorithm. The function should take three parameters: `start_value` (the initial value of the logistic map), `length` (the number of indicators to generate), and `r` (the growth rate of the logistic map). The function should return a tuple of length `length` containing the generated chaotic indicators.
"""

def create_chaos_indicators(start_value: float, length: int, r: float):
    def logistic_map(x, r):
        return r * x * (1 - x)

    indicators = []
    
    x = start_value
    
    for i in range(length):
        x = logistic_map(x, r)
        indicators.append(x)
        
    return tuple(indicators)