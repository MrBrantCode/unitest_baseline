"""
QUESTION:
Write a function `calculate_distance` that calculates the distance between two cars after the second car has traveled for 24 hours, given their respective speeds and the time spent during the day and night with speed reductions due to extra load. The first car travels 24 hours before the second car and the length of a day is 12 hours. The function should return the distance between the two cars after 24 hours of the second car's journey. 

The first car has an average speed of 68 km/h with 70% of the full journey duration during the day and 30% during the night. The second car has an average speed of 75 km/h, with 60% of the total travel time during daylight hours and 40% during nighttime. Both cars have an extra load that reduces their speed by 15% during the first half of their daytime journey and by 10% for the first half of their nighttime journey.
"""

def calculate_distance(car1_speed, car1_day_percentage, car1_night_percentage, car2_speed, car2_day_percentage, car2_night_percentage):
    day_length = 12
    car1_extra_load_day_reduction = 0.15
    car1_extra_load_night_reduction = 0.10
    car2_extra_load_day_reduction = 0.15
    car2_extra_load_night_reduction = 0.10
    
    # For first car
    first_car_first_half_day_distance = (day_length * car1_day_percentage * 0.5) * (car1_speed * (1 - car1_extra_load_day_reduction))
    first_car_second_half_day_distance = (day_length * car1_day_percentage * 0.5) * car1_speed

    first_car_first_half_night_distance = (day_length * car1_night_percentage * 0.5) * (car1_speed * (1 - car1_extra_load_night_reduction))
    first_car_second_half_night_distance = (day_length * car1_night_percentage * 0.5) * car1_speed

    # As the first car travels for 48 hours, we multiply each portion by 4
    total_first_car_distance = 4 * (first_car_first_half_day_distance + first_car_second_half_day_distance + first_car_first_half_night_distance + first_car_second_half_night_distance)

    # For second car
    second_car_first_half_day_distance = (day_length * car2_day_percentage * 0.5) * (car2_speed * (1 - car2_extra_load_day_reduction))
    second_car_second_half_day_distance = (day_length * car2_day_percentage * 0.5) * car2_speed

    second_car_first_half_night_distance = (day_length * car2_night_percentage * 0.5) * (car2_speed * (1 - car2_extra_load_night_reduction))
    second_car_second_half_night_distance = (day_length * car2_night_percentage * 0.5) * car2_speed

    # As the second car travels for 24 hours, we multiply each portion by 2
    total_second_car_distance = 2 * (second_car_first_half_day_distance + second_car_second_half_day_distance + second_car_first_half_night_distance + second_car_second_half_night_distance)

    distance_between_cars = total_first_car_distance - total_second_car_distance
    return distance_between_cars

# Using example values
car1_speed = 68
car1_day_percentage = 0.7
car1_night_percentage = 0.3
car2_speed = 75
car2_day_percentage = 0.6
car2_night_percentage = 0.4

print(calculate_distance(car1_speed, car1_day_percentage, car1_night_percentage, car2_speed, car2_day_percentage, car2_night_percentage))