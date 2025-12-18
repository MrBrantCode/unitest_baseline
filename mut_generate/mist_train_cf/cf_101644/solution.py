"""
QUESTION:
Create a function `calculate_launch_probability` that takes in a JSON object containing the positions of Jupiter, Venus, and Saturn as lists of three numbers each. Calculate the average of the three positions, subtract the average from each planet's position, square the results, sum them up, and take the square root to get the distance. Then, calculate the probability by taking the inverse of the distance, multiplying by 100, and rounding to two decimal places. The function should return the calculated probability. The input JSON object should have the following format: `{"jupiter_pos": [x1, y1, z1], "venus_pos": [x2, y2, z2], "saturn_pos": [x3, y3, z3]}`.
"""

import math

def calculate_launch_probability(data):
    """
    Calculate the probability of a successful rocket launch based on the positions of Jupiter, Venus, and Saturn.

    Args:
    data (dict): A dictionary containing the positions of Jupiter, Venus, and Saturn as lists of three numbers each.
                 The dictionary should have the following format: 
                 {"jupiter_pos": [x1, y1, z1], "venus_pos": [x2, y2, z2], "saturn_pos": [x3, y3, z3]}

    Returns:
    float: The calculated probability of a successful rocket launch.
    """
    # get the positions of Jupiter, Venus, and Saturn
    jupiter_pos = data['jupiter_pos']
    venus_pos = data['venus_pos']
    saturn_pos = data['saturn_pos']

    # calculate the average position
    avg_pos = [(jupiter_pos[i] + venus_pos[i] + saturn_pos[i]) / 3 for i in range(3)]

    # calculate the distance
    distance = math.sqrt(sum([(jupiter_pos[i]-avg_pos[i])**2 + (venus_pos[i]-avg_pos[i])**2 + (saturn_pos[i]-avg_pos[i])**2 for i in range(3)]))

    # calculate the probability
    probability = round((1/distance)*100, 2)

    return probability