"""
QUESTION:
Write a function `Race` that takes three arguments: `time_to_finish_car`, `time_to_finish_train`, and `time`. The function should calculate the distances of the car and the train from the starting point after the provided time, and also the difference between their distances. The function should assume a 1-unit distance for the race and calculate the speeds of the car and the train based on the given finish times.
"""

def Race(time_to_finish_car, time_to_finish_train, time):
    speed_train = 1 / float(time_to_finish_train)
    speed_car = 1 / float(time_to_finish_car)
    
    distance_train = time * speed_train
    distance_car = time * speed_car
    
    return distance_train, distance_car, distance_train - distance_car