"""
QUESTION:
Implement a function named `detect_temperature_periods` that takes a list of 72 hourly temperature readings, a lower temperature limit, an upper temperature limit, a minimum duration of consecutive hours, and a tolerance value. The function should return a list of tuples, where each tuple contains the start and end times of contiguous periods with temperatures outside the limits (with consideration for the tolerance value) and the duration of these periods. The function should also print a warning if the temperature exceeds the upper or lower limit beyond the specified tolerance value. The function should only include periods that meet or exceed the minimum duration of consecutive hours.
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