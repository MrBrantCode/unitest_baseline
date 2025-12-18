"""
QUESTION:
Write a function `calculate_average_weight` that takes a list of dictionaries `animals_list` and a string `authorized_personnel` as input. Each dictionary in `animals_list` should contain the keys 'name', 'weight_august', and 'species'. The function should only allow access if `authorized_personnel` is "zoo_keeper". It should filter out any negative weights and weights above 1000, calculate the average weight of the remaining animals, and return the average weight rounded to two decimal places. If no valid weights are found, the function should return "No valid weights found". If access is denied, the function should return "Access denied".
"""

def calculate_average_weight(animals_list, authorized_personnel):
    # check if the user is authorized
    if authorized_personnel != "zoo_keeper":
        return "Access denied"
    
    # filter out negative values and outliers
    valid_weights = [animal["weight_august"] for animal in animals_list if animal["weight_august"] > 0 and animal["weight_august"] <= 1000]
    
    # check if there are any valid weights
    if len(valid_weights) == 0:
        return "No valid weights found"
    
    # calculate the average weight
    average_weight = sum(valid_weights) / len(valid_weights)
    
    # round off to two decimal places
    average_weight = round(average_weight, 2)
    
    return average_weight