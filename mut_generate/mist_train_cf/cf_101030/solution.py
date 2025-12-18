"""
QUESTION:
Write a function `calculate_average_weight` that calculates the average weight of all animals in the zoo for the month of August. The function should take two arguments: `animals_list`, a list of dictionaries containing animal data with keys 'name', 'weight_august', and 'species', and `authorized_personnel`, a string representing the authorized personnel who can access the data. The function should implement data validation measures to filter out negative values and outliers (weights less than 0 or greater than 1000) and access control measures to only allow authorized personnel to access the data. The function should return the average weight as a float, rounded to two decimal places, or a message indicating that the user is not authorized or that no valid weights were found.
"""

def calculate_average_weight(animals_list, authorized_personnel):
    if authorized_personnel != "zoo_keeper":
        return "Access denied"
    
    valid_weights = [animal["weight_august"] for animal in animals_list if animal["weight_august"] > 0 and animal["weight_august"] < 1000]
    
    if len(valid_weights) == 0:
        return "No valid weights found"
    
    average_weight = sum(valid_weights) / len(valid_weights)
    
    return round(average_weight, 2)