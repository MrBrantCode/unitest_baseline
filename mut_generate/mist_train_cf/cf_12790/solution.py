"""
QUESTION:
Create a `Student` class with the following properties and methods:

- A constructor (`__init__`) that takes `name`, `age`, and `grade` as parameters.
- A method `add_attendance` that takes a boolean value (`True` for present, `False` for absent) and updates the student's attendance record.
- A method `get_attendance_percentage` that calculates the student's attendance percentage based on their attendance record.
- A method `is_honor_roll` that returns `True` if the student's grade is 90 or above and their attendance percentage is 95 or above, and `False` otherwise.
"""

def is_honor_roll(name, age, grade, attendance):
    total_days = len(attendance)
    present_days = sum(attendance)
    attendance_percentage = (present_days / total_days) * 100
    return grade >= 90 and attendance_percentage >= 95