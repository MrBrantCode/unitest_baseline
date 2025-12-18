"""
QUESTION:
Create a Python function `synodic_new_moon_return` that takes the degrees traveled by the new moon each synodic month as a float and returns a tuple containing the time taken for the new moon to return to the same nakshatra and the number of revolutions completed during this period. The time taken should be rounded to 6 decimal places and the input degrees_per_month should be a float representing the degrees traveled by the new moon each synodic month.
"""

def synodic_new_moon_return(degrees_per_month: float) -> tuple:
    time_taken = round(360 / degrees_per_month, 6)
    revolutions = int(time_taken)
    return (time_taken, revolutions)