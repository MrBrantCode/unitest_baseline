"""
QUESTION:
Develop a function named 'ship_distance' that calculates the distances of a fleet of ships from the port after 6 hours. The function should take three parameters: start_times (a list of times in hours when each ship increases its speed), initial_speeds (a list of the initial speeds of each ship in km/h), and num_ships (the total number of ships). Each ship increases its speed by 5 km/h at its specified time and maintains the new speed until the 6 hour mark. The function should return a list of distances, with each distance rounded to two decimal places.
"""

def ship_distance(start_times, initial_speeds, num_ships):
    distances = []
    
    for i in range(num_ships):
        if start_times[i] > 6:
            dist = initial_speeds[i] * 6
        else:
            dist = initial_speeds[i] * start_times[i] + (initial_speeds[i] + 5) * (6 - start_times[i])
        distances.append(round(dist, 2))
            
    return distances