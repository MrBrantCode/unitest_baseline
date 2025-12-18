"""
QUESTION:
Write a function `calculate_total_hours` that calculates the total hours worked by all employees. The function should take three parameters: `normal_shift` (the duration of a normal shift in hours), `days_for_work` (the number of days worked by each employee), and `overtime_workers` (the number of employees working overtime). The total hours worked should be calculated using the following steps:
1. Calculate the learning time as `days_for_work - days_for_work * 10 / 100`.
2. Calculate the regular hours worked as the product of the learning time and `normal_shift`.
3. Calculate the overtime hours worked as `overtime_workers * (2 * days_for_work)`.
4. Calculate the total hours worked as the sum of regular hours and overtime hours.
The function should return the total hours worked.
"""

def calculate_total_hours(normal_shift, days_for_work, overtime_workers):
    learn_time = days_for_work - days_for_work * 10 / 100
    hours_for_work = learn_time * normal_shift
    overtime = overtime_workers * (2 * days_for_work)
    all_time = hours_for_work + overtime
    return all_time