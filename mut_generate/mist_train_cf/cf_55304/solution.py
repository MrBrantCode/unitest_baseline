"""
QUESTION:
Create a function named `time_to_peak` that takes an initial velocity as input and returns the time it will take for a ball to reach its peak. The initial velocity must be a positive number and the time should be rounded to two decimal places. The acceleration due to gravity (g) is 9.8 m/s^2. If the input is invalid (not a positive number or non-numeric), the function should return an error message.
"""

def time_to_peak(initial_velocity):
    g = 9.8   # acceleration due to gravity in m/s^2
    
    try:
        initial_velocity = float(initial_velocity) # Try converting to float
        
        if initial_velocity <= 0: # If the value is not positive
            return "Invalid input, initial velocity must be positive"
        
        # calculate time taken to reach peak using the motion equation: v = u - gt
        time = (initial_velocity) / g
        return round(time, 2) # rounding off to two decimal places
        
    except ValueError: # If the conversion to float fails
        return "Invalid input, please enter a numeric value"