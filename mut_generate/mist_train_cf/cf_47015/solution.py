"""
QUESTION:
Write a function called `time_to_reach_heart_rate` that calculates the total time required to reach a target heart rate. The function should take five parameters: `resting_heart_rate`, `warmup_increase`, `exercise_increase`, `target_heart_rate`, and `warmup_time`. The function should return the total time in minutes. Assume that the warm-up exercise increases the heart rate at a constant rate for a fixed duration, after which the heart rate continues to increase at a different constant rate until the target heart rate is reached.
"""

def time_to_reach_heart_rate(resting_heart_rate, warmup_increase, exercise_increase, target_heart_rate, warmup_time):
    post_warmup_heart_rate = resting_heart_rate + (warmup_increase * warmup_time)
    required_increase = target_heart_rate - post_warmup_heart_rate
    exercise_time = required_increase / exercise_increase
    total_time = warmup_time + exercise_time
    return total_time