"""
QUESTION:
Create a function `process_time` that takes a start time, a duration, and a list of days as input and returns the end time after processing the duration. The start time is in the format "HH:MM AM/PM", the duration is in the format "HH:MM", and the list of days contains the days of the week. The function should handle the addition of the duration to the start time, accounting for any overflow in hours and days. The start time will always be in the correct format and the duration will not exceed 24 hours.
"""

def process_time(start_time, duration, days):
    # Split the start time into hours, minutes, and period (AM/PM)
    start_hour, start_minute = [int(t) for t in start_time[:-3].split(':')]
    start_minute, period = start_minute, start_time[-2:]
    start_hour = int(start_hour)
    start_minute = int(start_minute)

    # Split the duration into hours and minutes
    duration_hour, duration_minute = [int(d) for d in duration.split(':')]

    # Calculate the end time
    end_hour = start_hour + duration_hour
    end_minute = start_minute + duration_minute

    # Adjust for overflow in minutes
    if end_minute >= 60:
        end_hour += 1
        end_minute -= 60

    # Adjust for overflow in hours
    end_hour = end_hour % 12
    if end_hour == 0:
        end_hour = 12

    # Adjust for period (AM/PM)
    if period == 'AM' and end_hour >= 12:
        period = 'PM'
    elif period == 'PM' and end_hour < 12:
        period = 'AM'

    # Calculate the day offset
    day_offset = (start_hour + duration_hour) // 24
    start_day = days[0]
    end_day_index = (days.index(start_day) + day_offset) % len(days)
    end_day = days[end_day_index]

    # Format the end time
    end_time = f"{end_hour:02d}:{end_minute:02d} {period}"

    return end_time