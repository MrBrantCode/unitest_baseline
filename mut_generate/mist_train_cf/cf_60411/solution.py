"""
QUESTION:
Write a function `choose_num(x, y, z)` that takes three positive integers `x`, `y`, and `z` as input. The function should return the largest even integer number that is less than or equal to `y`, greater than or equal to `x`, and a multiple of `z`. If no such number exists, the function should return `None`. The function should handle potential exceptions, including non-integer inputs and invalid input values.
"""

def choose_num(x, y, z):
    """This function should take three positive numbers x, y, and z. The function must return 
    the largest even integer number that is less than or equal to y and greater than or equal 
    to x, which is also a multiple of z. In case no such number exists, the function should return None.
    
    Validate your code with the added complexity of handling potential exceptions.
    """  
    if not (type(x) == type(y) == type(z) == int):
        return "Error: Inputs must be integers."

    if not (x >= 0 and y >= 0 and z > 0):
        return "Error: Inputs must be positive and z should be greater than 0."

    if x > y:
        return "Error: x should be less than or equal to y."

    #Initialize the largest number as None.
    largest_num = None
    
    #Iterate from y to x both inclusive to find largest even multiple of z.
    for i in range(y, x - 1, -1):
        if i % z == 0 and i % 2 == 0:
            largest_num = i
            break
        
    #Return the largest number.
    return largest_num