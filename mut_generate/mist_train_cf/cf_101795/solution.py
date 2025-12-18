"""
QUESTION:
Create a function called `calculate_launch_probability` that takes a JSON object containing the positions of Jupiter, Venus, and Saturn as input. The positions are represented as lists of three numbers each. Calculate the probability of a rocket launch being successful based on these positions by following these steps: 

1. Calculate the average position of the three planets by adding their positions together and dividing by three.
2. Subtract the average position from each planet's position, square the result, and sum these squared values together.
3. Take the square root of the sum from step 2 and assign it to a variable called `distance`.
4. Calculate the probability by taking the inverse of `distance` and multiplying by 100.
5. Round the probability to two decimal places.

The function should return the calculated probability as a number.
"""

import json
import math

def calculate_launch_probability(data):
    """
    Calculate the probability of a rocket launch being successful based on the positions of Jupiter, Venus, and Saturn.

    Args:
        data (dict): A dictionary containing the positions of Jupiter, Venus, and Saturn as lists of three numbers each.

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