"""
QUESTION:
Write a function `time_difference` that takes two lists of time strings in the format "HH:MM:SS" as input. Calculate the average duration in seconds between each pair of corresponding times from the two lists, considering cases where the first time might be later than the second time, implying that the time spanned across the next day. Also, calculate the overall average duration across all pairs. The input lists are guaranteed to be of equal length and contain valid times in 24-hour format. The function should handle lists of up to 10^5 times each efficiently.
"""

from datetime import datetime, timedelta

def time_difference(list_1, list_2):
    # Convert lists to datetime objects
    times_1 = [datetime.strptime(time, "%H:%M:%S") for time in list_1]
    times_2 = [datetime.strptime(time, "%H:%M:%S") for time in list_2]

    # Calculate the difference between each pair
    differences = []
    for i in range(len(times_1)):
        difference = times_2[i] - times_1[i]
        # If the time spanned to the next day
        if difference.days < 0:
            difference += timedelta(days=1)
        differences.append(difference)

    # Convert differences to seconds
    differences_seconds = [diff.total_seconds() for diff in differences]

    # Calculate average duration for each pair
    pair_averages = [diff / 2 for diff in differences_seconds]

    # Calculate the overall average
    overall_average = sum(differences_seconds) / (2 * len(differences_seconds))

    return pair_averages, overall_average