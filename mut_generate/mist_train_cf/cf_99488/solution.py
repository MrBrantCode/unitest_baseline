"""
QUESTION:
Create a function named `calculate_average_hr_bp` that takes in two lists of numbers representing heart rate data and blood pressure data. The function should return the average heart rate and average blood pressure. The heart rate data is in beats per minute and the blood pressure data is in millimeters of mercury (mmHg).
"""

def calculate_average_hr_bp(hr_data, bp_data):
    avg_hr = sum(hr_data) / len(hr_data)
    avg_bp = sum(bp_data) / len(bp_data)
    return avg_hr, avg_bp