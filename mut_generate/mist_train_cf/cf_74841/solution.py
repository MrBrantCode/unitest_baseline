"""
QUESTION:
Create a function named `complex_calculations` that takes two complex numbers as input, calculates the magnitude and phase of each number, squares these values, and returns the sum of the squared magnitude and phase values. The function should handle any errors that occur during type conversion or calculation and provide a corresponding error message.
"""

import cmath

def complex_calculations(c1, c2):
    try:
        # Extract the magnitude and phase of each complex number
        mag1, phase1 = cmath.polar(c1)
        mag2, phase2 = cmath.polar(c2)
        
        # Square the magnitude and phase of each complex number
        mag1_squared = mag1 ** 2
        phase1_squared = phase1 ** 2
        mag2_squared = mag2 ** 2
        phase2_squared = phase2 ** 2
        
        # Sum the squared values
        total = mag1_squared + phase1_squared + mag2_squared + phase2_squared
        
        return total
    
    except TypeError as e:
        # Handle any errors in type conversion
        print("Error: input values must be complex numbers (i.e., of the form a + bj).")
        print(f"TypeError: {e}")
        
    except ValueError as e:
        # Handle any errors in calculation
        print("Error: a mathematical operation failed.")
        print(f"ValueError: {e}")