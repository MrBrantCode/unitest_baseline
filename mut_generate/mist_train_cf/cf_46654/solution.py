"""
QUESTION:
Create a function called `calculate_metal_ore_weights` that takes in the total weight of the mixed metal ore crate and the weights of the four different types of metal ores (iron, copper, nickel, and zinc) as input. The function should return a dictionary with the weights of each type of metal ore required to create the crate. Assume the input weights of the metal ores are in the same ratio as given in the example (3:4:2:1).
"""

def calculate_metal_ore_weights(total_weight):
    """
    Calculate the weights of each type of metal ore required to create a mixed metal ore crate.

    Args:
        total_weight (int): The total weight of the mixed metal ore crate.

    Returns:
        dict: A dictionary with the weights of each type of metal ore (iron, copper, nickel, zinc) required.

    """
    # The ratio of weights of the metal ores (iron, copper, nickel, zinc)
    ratio = [3, 4, 2, 1]
    total_ratio = sum(ratio)
    multiplier = total_weight / total_ratio

    # Calculate the weights of each type of metal ore
    iron_weight = ratio[0] * multiplier
    copper_weight = ratio[1] * multiplier
    nickel_weight = ratio[2] * multiplier
    zinc_weight = ratio[3] * multiplier

    # Return a dictionary with the weights of each type of metal ore
    return {
        'iron': iron_weight,
        'copper': copper_weight,
        'nickel': nickel_weight,
        'zinc': zinc_weight
    }