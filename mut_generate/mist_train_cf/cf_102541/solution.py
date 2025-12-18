"""
QUESTION:
Create a function called "rotate_array" that takes in two parameters: an array of integers and a positive or negative integer representing the number of positions to rotate. The function should rotate the elements of the array to the right if the positions are positive and to the left if the positions are negative. If the positions are 0, return the original array. Return the rotated array.
"""

def rotate_array(array, positions):
    if positions > 0:
        positions = positions % len(array)
        return array[-positions:] + array[:-positions]
    elif positions < 0:
        positions = abs(positions) % len(array)
        return array[positions:] + array[:positions]
    else:
        return array