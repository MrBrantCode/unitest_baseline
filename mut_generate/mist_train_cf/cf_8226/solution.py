"""
QUESTION:
Create a function named `get_day_name` that takes an integer `day` as input, where `1 <= day <= 1000`. The function should return the corresponding day of the week for the year 2022, taking into account leap years. If the input `day` is not within the specified range, the function should return an error message. Assume January 1, 2022 is a Saturday.
"""

def get_day_name(day):
    # Check if the input is within the specified range
    if day < 1 or day > 1000:
        return "Error: Input should be between 1 and 1000 (inclusive)."

    # Define a list of day names
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    # Define days in a month for 2022
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Initialize day of week index to Saturday (January 1, 2022)
    day_index = 5
    
    # Iterate over each month in 2022
    for month in range(12):
        if day > days_in_month[month]:
            day -= days_in_month[month]
        else:
            # Calculate the day of the week using the remaining days
            day_index = (day_index + day - 1) % 7
            return days_of_week[day_index]

    # Return the corresponding day name
    return days_of_week[day_index]