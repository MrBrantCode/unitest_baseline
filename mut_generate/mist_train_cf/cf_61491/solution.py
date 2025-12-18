"""
QUESTION:
Create three functions, `calculate_z(x)`, `calculate_x(z)`, and `substitute(z, x)`, to solve the equation 4z = 20 - 2x, with the constraints that both z and x must be integers and within the range -100 to 100. The functions should return the calculated values of z, x, and a boolean indicating whether the equation holds true when both z and x are substituted back into the equation. If any input or calculated value is out of bounds, return an error message.
"""

def calculate_z(x):
    if isinstance(x, int) and -100 <= x <= 100:
        z = (20 - 2*x) / 4
        if -100 <= z <= 100:
            return int(z)
        else:
            return "Value of z is out of bounds: -100 <= z <= 100"
    else:
        return "Invalid input or x is out of bounds: -100 <= x <= 100"

def calculate_x(z):
    if isinstance(z, int) and -100 <= z <= 100:
        x = (20 - 4*z) / 2
        if -100 <= x <= 100:
            return int(x)
        else:
            return "Value of x is out of bounds: -100 <= x <= 100"
    else:
        return "Invalid input or z is out of bounds: -100 <= z <= 100"

def substitute(z, x):
    if (isinstance(z, int) and -100 <= z <= 100) and (isinstance(x, int) and -100 <= x <= 100):
        return 4*z == 20 - 2*x
    else:
        return "Invalid inputs or x, z is out of bounds: -100 <= x, z <= 100"