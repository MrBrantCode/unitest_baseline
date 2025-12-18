"""
QUESTION:
Implement a function `time_to_minutes(days, hours, minutes)` that takes three inputs representing durations in days, hours, and minutes. The function should sort these durations from longest to shortest, convert them to equivalent minutes, and return the sorted list. Ensure the function includes exception handling for invalid inputs, where days and hours are non-negative integers, and minutes are integers between 0 and 59.
"""

def time_to_minutes(days, hours, minutes):
    """
    This function converts input durations in days, hours, and minutes to minutes.
    """
    try:
        # Input validation
        assert type(days) == int and days >=0, "Days should be a non-negative integer"
        assert type(hours) == int and hours >=0, "Hours should be a non-negative integer"
        assert type(minutes) == int and 0 <= minutes <= 59, "Minutes should be an integer between 0 and 59"

        # Converting all durations to minutes
        days_in_minutes = days * 24 * 60
        hours_in_minutes = hours * 60

        # Sorted list of durations
        sorted_durations = sorted([days_in_minutes, hours_in_minutes, minutes], reverse=True)

        return sorted_durations

    except AssertionError as msg:  
        print(msg) 
    except Exception as e:
        print(f"Error: {e}")