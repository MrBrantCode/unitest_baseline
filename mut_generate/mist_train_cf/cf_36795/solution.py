"""
QUESTION:
Implement the function `calculate_average_seebeck(seebeck_coefficients)` that takes in a nested dictionary `seebeck_coefficients` representing Seebeck coefficients at different conditions and returns a dictionary containing the average Seebeck coefficient for each type of charge carrier (n-type and p-type) at each temperature.

The input dictionary `seebeck_coefficients` is structured as follows:
- It has two main keys: "n" and "p", representing the type of charge carrier.
- Each charge carrier has multiple temperatures as keys, and each temperature has multiple conditions as keys.
- The values for each condition are lists of Seebeck coefficients.

The returned dictionary should have the same structure as the input, but with the values being the average Seebeck coefficients for each condition at each temperature, rounded to two decimal places.

Restrictions: 
- All conditions must have the same number of measurements.
- The function should calculate the average Seebeck coefficient for each condition across all charge carriers.
"""

def calculate_average_seebeck(seebeck_coefficients):
    average_seebeck = {"n": {}, "p": {}}

    for carrier in ["n", "p"]:
        for temperature, conditions in seebeck_coefficients[carrier].items():
            average_seebeck[carrier][temperature] = {}
            for condition, values in conditions.items():
                num_measurements = len(values[0])  
                avg_values = [sum(measurement) / num_measurements for measurement in zip(*values)]
                average_seebeck[carrier][temperature][condition] = round(sum(avg_values) / len(avg_values), 2)

    return average_seebeck