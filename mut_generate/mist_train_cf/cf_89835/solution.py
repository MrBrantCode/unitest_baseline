"""
QUESTION:
Create a function called `clamp` that takes three parameters: a number and a minimum and maximum value, all of which can be floating-point numbers. If the number is negative, return its absolute value before clamping. If the absolute number is less than the minimum, return either the minimum or a string indicating its proximity to the minimum if it's within 5% of the minimum. If the absolute number is greater than the maximum, return either the maximum or a string indicating its proximity to the maximum if it's within 5% of the maximum. If the absolute number is between the minimum and maximum, return the number. The function should have a time complexity of O(1) and space complexity of O(1).
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