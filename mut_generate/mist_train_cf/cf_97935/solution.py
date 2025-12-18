"""
QUESTION:
Write a function `calculate_average_hr_bp` that calculates the average heart rate and blood pressure given two lists of data: `hr_data` and `bp_data`. The function should take into account that the heart rate data is in beats per minute and the blood pressure data is in millimeters of mercury (mmHg). The function should return two values: the average heart rate and the average blood pressure.
"""

def calculate_average_hr_bp(hr_data, bp_data):
    avg_hr = sum(hr_data) / len(hr_data)
    avg_bp = sum(bp_data) / len(bp_data)
    return avg_hr, avg_bp