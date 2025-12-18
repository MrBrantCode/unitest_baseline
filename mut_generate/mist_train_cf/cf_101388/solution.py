"""
QUESTION:
Design a Python function `filter_retreats` that takes in a list of retreat centers (`retreats_list`), a specific location, a maximum budget, and a specific duration. The function should filter the list to include only retreat centers that match the specified location, have a budget less than or equal to the maximum budget, and have a duration that matches the specified duration. The function should return the filtered list of retreat centers.
"""

def filter_retreats(retreats_list, location, budget, duration):
    filtered_retreats = []
    for retreat in retreats_list:
        if retreat['location'] == location:
            if retreat['budget'] <= budget and retreat['duration'] == duration:
                filtered_retreats.append(retreat)
    return filtered_retreats