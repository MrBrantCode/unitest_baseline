"""
QUESTION:
You were given a string of integer temperature values. Create a function `close_to_zero(t)` and return the closest value to 0 or `0` if the string is empty. If two numbers are equally close to zero, return the positive integer.
"""

def closest_to_zero(t: str) -> int:
    if not t:
        return 0
    
    temperatures = list(map(int, t.split()))
    
    if not temperatures:
        return 0
    
    closest = temperatures[0]
    
    for temp in temperatures:
        if abs(temp) < abs(closest) or (abs(temp) == abs(closest) and temp > closest):
            closest = temp
    
    return closest