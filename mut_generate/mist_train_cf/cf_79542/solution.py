"""
QUESTION:
Create a function named `convert_floats` that takes an array of floating-point numbers as input. The function should return a new array where each number is rounded to the nearest whole number. However, if any number in the input array is outside the range -100 to 100, the function should return 'Error' for that number. If the input array is empty or null, the function should return an empty array.
"""

def convert_floats(array):
    if array is None or len(array) == 0:
        return []
    results = []
    for num in array:
        if -100 <= num <= 100:
            results.append(round(num))
        else:
            results.append('Error')
    return results