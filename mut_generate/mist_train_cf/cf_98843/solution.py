"""
QUESTION:
Create a function called 'calculate_missed_days' that takes a 2D list of integers representing the number of days missed during each weekday over a period of weeks. The function should return a string that includes the total number of missed school days. 

The 2D list has the following structure: [[Monday, Tuesday, Wednesday, Thursday, Friday], ...] for each week. The function should also provide a written justification of how the missed school days will impact the student's academic progress.

The total number of missed school days should be calculated by summing all the days missed across all weeks and weekdays. The justification should include a detailed plan outlining how the school will support the student's academic success despite the missed school days.
"""

def calculate_missed_days(days_missed):
    """
    Calculate the total number of missed school days.

    Args:
    days_missed (list): A 2D list of integers representing the number of days missed during each weekday over a period of weeks.

    Returns:
    str: A string including the total number of missed school days and a justification for the impact on the student's academic progress.
    """
    total_missed = sum(sum(week) for week in days_missed)
    justification = f"The student's absence from school during the weekdays has resulted in a total of {total_missed} missed days. " \
                   f"This level of absence can significantly impact the student's academic progress, and as a result, we must take steps " \
                   f"to support the student's success. To address this issue, we will work with the student to develop a plan that " \
                   f"includes additional tutoring, make-up work, and other resources to ensure that the student can catch up on missed material. " \
                   f"Additionally, we will closely monitor the student's progress to ensure that she stays on track and receives the necessary " \
                   f"support to achieve academic success."
    return f"The total number of missed school days is: {total_missed}. {justification}"