"""
QUESTION:
Create a function named `calculate_missed_days` that takes a 2D list `days_table` representing the number of days missed during each weekday over a period of four weeks and returns a tuple containing the total number of missed school days and a justification of how the missed school days will impact the student's academic progress.
"""

def calculate_missed_days(days_table):
    total_missed = sum(sum(row) for row in days_table)
    justification = f"The student's absence from school during the weekdays has resulted in a total of {total_missed} missed days over a period of four weeks. This level of absence can significantly impact the student's academic progress, and as a result, we must take steps to support the student's success."
    return total_missed, justification