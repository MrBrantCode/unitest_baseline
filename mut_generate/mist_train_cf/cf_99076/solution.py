"""
QUESTION:
Design a Python function `filter_retreats` that takes in a list of retreat centers and filters them based on specific attributes. The function should have the following parameters: `retreats_list`, `location`, `budget`, and `duration`. The function should return a list of retreat centers that match the specified location, have a budget less than or equal to the specified budget, and have a duration equal to the specified duration.
"""

def filter_retreats(retreats_list, location, budget, duration):
    filtered_retreats = []
    for retreat in retreats_list:
        if retreat['location'] == location:
            if retreat['budget'] <= budget and retreat['duration'] == duration:
                filtered_retreats.append(retreat)
    return filtered_retreats