"""
QUESTION:
Write a function, `car_speeds(distance, time, speed_difference)`, that determines the speeds of two cars, A and B, traveling in opposite directions. The function should accept three parameters: the total distance between the cars after a certain time, the duration of travel, and the speed difference between the two cars. The function should return a tuple with two elements, representing the speeds of car A and car B, respectively. Use numerical methods to solve for the speeds, given that car A's speed is X km/h and car B's speed is X + `speed_difference` km/h.
"""

def car_speeds(distance, time, speed_difference):
    speedA = 0 
    while True:
        speedB = speedA + speed_difference
        if abs((speedA *time + speedB * time) - distance) <= 0.0001: 
            return (speedA, speedB) 
        speedA += 0.0001 