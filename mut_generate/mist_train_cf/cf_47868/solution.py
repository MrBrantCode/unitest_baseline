"""
QUESTION:
Write a function `calculate_average_speed` that takes an array `speed_data` representing the car's speed in km/h recorded every minute and returns the average speed of the car for the entire journey. The distance between points A and B is 1 km for each minute record. The speed at each time point does not represent the total distance traveled, but rather the speed per minute unit. Assume each speed record corresponds to one minute. The average speed should be calculated using the formula: Average speed = Total distance traveled / Total time taken.
"""

def calculate_average_speed(speed_data):
  total_distance = 0
  
  # Convert speed from km/h to km/min by dividing it by 60
  for speed in speed_data:
    total_distance += speed / 60 
    
  total_time = len(speed_data)
  
  return total_distance/total_time