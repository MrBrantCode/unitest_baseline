"""
QUESTION:
Create a function named `clamp` that takes in three floating-point numbers: `number`, `minimum`, and `maximum`. The function should return the absolute value of `number` if it is negative, then clamp it to the range defined by `minimum` and `maximum`. If the clamped `number` is within 5% of `minimum` or `maximum`, return a string indicating its proximity to the range boundary; otherwise, return the clamped `number`. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def clamp(number, minimum, maximum):
    if number < 0:
        number = abs(number)
    
    if number < minimum:
        if minimum - number <= 0.05 * minimum:
            return "Number is within 5% of the minimum value"
        else:
            return minimum
    
    if number > maximum:
        if number - maximum <= 0.05 * maximum:
            return "Number is within 5% of the maximum value"
        else:
            return maximum
    
    return number