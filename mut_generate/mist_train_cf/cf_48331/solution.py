"""
QUESTION:
Create a function named `original_weights` that takes a list of three weights as input. The function should first validate the input data to ensure that there are exactly three weights, all of which are positive numbers, and their total does not exceed 37 kilograms. Then, it should correct the erroneous sequence of the pots and calculate the original weights of honey in each pot. The weights of the pots are in the ratio of 4:3 (Pot x to Pot y after 3.5 kilograms are removed from Pot x) and 3:2 (Pot y to Pot z). The function should return a dictionary with the original weights of honey in each pot, labeled as "Pot x", "Pot y", and "Pot z".
"""

def original_weights(weights):
    if len(weights) != 3: 
        return "Error: Invalid data. Please input the weights of three pots."
    
    for w in weights: 
        if not isinstance(w, (int, float)) or w < 0: 
            return "Error: Invalid data. Please enter positive numbers only."
        if sum(weights) > 37: 
            return "Error: The total weight exceeds 37 kilograms. Please enter valid weights."

    weights.sort()
    ratios = [(w-3.5, w, w*3/2) for w in weights]
    for r in ratios: 
        if abs(r[0] / r[1] - 4/3) < 0.01 and abs(r[1] / r[2] - 3/2) < 0.01: 
            return {"Pot x": r[0]+3.5, "Pot y": r[1], "Pot z": r[2]}

    return "Unable to determine weights. Please check the data."