"""
QUESTION:
Write a function `calculate_distances(train_time, car_times)` that takes the train's finish time and a list of car finish times as input, and returns the indices of the closest and farthest cars from the train after `train_time` minutes. The function should assume that all vehicles maintain a constant speed throughout the race and should be efficient to handle large datasets (up to 10^6 cars).
"""

from bisect import bisect_left

def calculate_distances(train_time, car_times):
    car_times.sort()

    # Find position of a train in sorted list
    pos = bisect_left(car_times, train_time)

    closest_car = None
    closest_distance = float("inf")
    farthest_car = None
    farthest_distance = float("-inf")

    for i, finish_time in enumerate(car_times):
        distance = abs(finish_time - train_time)

        if distance < closest_distance:
            closest_distance = distance
            closest_car = i + 1

        if distance > farthest_distance:
            farthest_distance = distance
            farthest_car = i + 1

    return closest_car, farthest_car