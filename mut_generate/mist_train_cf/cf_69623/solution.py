"""
QUESTION:
Write a function named `calculate_honey_weights` to find the original weights of honey in three distinct pots. The total weight of the honey in the three pots is 37 kilograms. After 3.5 kilograms of honey is used from the largest pot, the weight ratio of the honey in the first pot to the second pot is 4:3, and the weight ratio of the honey in the second pot to the third pot is 3:2. Return a list of the original weights of honey in each of the three distinct pots in kilograms.
"""

def calculate_honey_weights(total_weight, used_honey, ratio1, ratio2):
    x = (used_honey * ratio1[1] * ratio2[1]) / (ratio1[0] * ratio2[1] - ratio1[1] * ratio2[0])
    first_pot_weight = (ratio1[0] / (ratio1[0] + ratio1[1])) * x + used_honey
    second_pot_weight = (ratio1[1] / (ratio1[0] + ratio1[1])) * x
    third_pot_weight = total_weight - x
    return [first_pot_weight, second_pot_weight, third_pot_weight]

def calculate_honey_weights_v2():
    total_weight = 37
    used_honey = 3.5
    ratio1 = [4, 3]
    ratio2 = [3, 2]
    return calculate_honey_weights(total_weight, used_honey, ratio1, ratio2)