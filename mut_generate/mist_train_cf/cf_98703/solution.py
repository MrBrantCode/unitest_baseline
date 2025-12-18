"""
QUESTION:
Write a Python function `calculate_average_weight` that calculates the average weight of all animals in the zoo for the month of August. The function should take two arguments: `animals_list`, a list of dictionaries containing animal data, and `authorized_personnel`, a string representing the authorized personnel who can access the data. Each dictionary in `animals_list` should contain the keys `name`, `weight_august`, and `species`. The function should implement data validation measures by removing any negative values or outliers (defined as weights greater than 1000) from the list of weights. The function should also implement access control measures by only allowing authorized personnel ("zoo_keeper") to access the data. The function should return the average weight as a float, rounded to two decimal places.
"""

def calculate_average_weight(animals_list, authorized_personnel):
    # check if the user is authorized
    if authorized_personnel != "zoo_keeper":
        return "Access denied"
    
    # filter out negative values and outliers
    valid_weights = [animal["weight_august"] for animal in animals_list if animal["weight_august"] > 0 and animal["weight_august"] < 1000]
    
    # check if there are any valid weights
    if len(valid_weights) == 0:
        return "No valid weights found"
    
    # calculate the average weight
    average_weight = sum(valid_weights) / len(valid_weights)
    
    # round off to two decimal places
    average_weight = round(average_weight, 2)
    
    return average_weight