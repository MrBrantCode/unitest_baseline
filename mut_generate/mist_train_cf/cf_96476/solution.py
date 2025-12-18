"""
QUESTION:
Write a function named `calculate_cubes` that takes an array of integers as input and returns a new array where each element is the cube of the corresponding element in the input array. The function should not use any arithmetic operators or built-in functions to calculate the cubes.
"""

def calculate_cubes(nums):
    cube_array = []

    for num in nums:
        result = 0
        counter = 0

        while counter < num:
            result = (result << 3)
            counter += 1
        
        cube_array.append(result)

    return cube_array