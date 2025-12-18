"""
QUESTION:
Fast & Furious Driving School's (F&F) charges for lessons are as below: 



Time
Cost


Up to 1st hour
$30


Every subsequent half hour**
$10


** Subsequent charges are calculated by rounding up to nearest half hour.


For example, if student X has a lesson for 1hr 20 minutes, he will be charged $40 (30+10) for 1 hr 30 mins and if he has a lesson for 5 minutes, he will be charged $30 for the full hour. 

Out of the kindness of its heart, F&F also provides a 5 minutes grace period. So, if student X were to have a lesson for 65 minutes or 1 hr 35 mins, he will only have to pay for an hour or 1hr 30 minutes respectively. 

For a given lesson time in minutes (min) , write a function price to calculate how much the lesson costs.
"""

import math

def calculate_lesson_cost(lesson_time_minutes: int) -> int:
    # Apply the grace period
    effective_time = max(0, lesson_time_minutes - 5)
    
    # Calculate the base cost for the first hour
    base_cost = 30
    
    # Calculate the additional cost for every subsequent half hour
    additional_time = max(0, effective_time - 60)
    additional_cost = 10 * math.ceil(additional_time / 30)
    
    # Total cost is the sum of base cost and additional cost
    total_cost = base_cost + additional_cost
    
    return total_cost