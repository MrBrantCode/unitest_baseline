"""
QUESTION:
Write a function `enhanced_lowest_common_multiple(x, y)` that calculates the Least Common Multiple (LCM) of two numbers `x` and `y`. The function should handle non-integer inputs and negative integers by returning an error message. The function should take two parameters, both of which must be integers greater than zero. If either condition is not met, the function should return "Error: Both numbers must be integers" or "Error: Both numbers must be positive" respectively.
"""

def enhanced_lowest_common_multiple(x, y):
    try:
        # Convert inputs to integers
        x = int(x)
        y = int(y)
        # Check if inputs are positive
        if x < 0 or y < 0:
            return "Error: Both numbers must be positive"
        # Compute LCM
        if x > y:
           greater = x
        else:
           greater = y

        while(True):
           if((greater % x == 0) and (greater % y == 0)):
               lcm = greater
               break
           greater += 1

        return lcm
    except ValueError:
        return "Error: Both numbers must be integers"