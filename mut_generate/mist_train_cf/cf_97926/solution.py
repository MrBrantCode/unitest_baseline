"""
QUESTION:
Develop a function named `detect_temperature_periods` that takes the following parameters: a list of temperatures recorded every hour, a lower limit, an upper limit, a duration of consecutive hours, and a tolerance value. The function should detect contiguous periods of time with temperature above or below the limits with the specified duration of consecutive hours, and return a list of tuples containing the start and end times of these periods as well as their duration in hours. If the temperature exceeds the upper or lower limit beyond the specified tolerance value, the function should provide a warning message. The function should also output the overall duration of the readings, which is 72 hours.
"""

def detect_temperature_periods(temperatures, lower_limit, upper_limit, duration, tolerance):
    """
    This function takes a list of temperatures recorded every hour for 72 hours, lower and upper limit, duration of
    consecutive hours, and a tolerance value to detect contiguous periods of time with temperature above or below
    the limits with the specified duration of consecutive hours. The function returns a list of tuples, where each
    tuple contains the start and end times of the contiguous period as well as its duration in hours.
    """
    start_time = end_time = None
    periods = []
    exceed_warning = False
    
    for i in range(len(temperatures)):
        if temperatures[i] > upper_limit + tolerance:
            exceed_warning = True
        elif temperatures[i] < lower_limit - tolerance:
            exceed_warning = True
        else:
            exceed_warning = False
            
        if temperatures[i] > upper_limit or temperatures[i] < lower_limit:
            if not start_time:
                start_time = i
            end_time = i
        else:
            if start_time and end_time and end_time - start_time + 1 >= duration:
                periods.append((start_time, end_time, end_time - start_time + 1))
            start_time = end_time = None
    
    if start_time and end_time and end_time - start_time + 1 >= duration:
        periods.append((start_time, end_time, end_time - start_time + 1))
    
    if exceed_warning:
        print("Warning: temperature exceeded the upper/lower limit beyond the specified tolerance value!")
        
    return periods