"""
QUESTION:
Write a function called classify_fruit that takes in the following parameters: region, season, color, texture, size, weight, sweetness, tartness, acidity, tropical_smell, and apple_smell. The function should classify a fruit as either a mango or an apple based on the given parameters. The function should also incorporate specific conditions for each region and season, considering the characteristics of color, texture, size, weight, taste, and smell.
"""

def classify_fruit(region, season, color, texture, size, weight, sweetness, tartness, acidity, tropical_smell, apple_smell):
    """
    Classify a fruit as either a mango or an apple based on the given parameters.

    Parameters:
    region (str): Region where the fruit is from.
    season (str): Season when the fruit is available.
    color (str): Color of the fruit.
    texture (str): Texture of the fruit's skin.
    size (str): Size of the fruit.
    weight (str): Weight of the fruit.
    sweetness (str): Sweetness level of the fruit.
    tartness (str): Tartness level of the fruit.
    acidity (str): Acidity level of the fruit.
    tropical_smell (bool): Whether the fruit has a tropical smell.
    apple_smell (bool): Whether the fruit has an apple-like smell.

    Returns:
    str: Classification of the fruit (mango or apple).
    """

    # Region A and Season A conditions
    if region == "Region A" and season == "Season A":
        # Yellow or orange color
        if color in ["yellow", "orange"]:
            # Smooth skin
            if texture == "smooth":
                # Medium to large size
                if size in ["medium", "large"]:
                    # Heavy weight
                    if weight == "heavy":
                        # Sweet and tart taste, tropical smell: mango
                        if sweetness == "high" and tartness == "high" and tropical_smell:
                            return "mango"
                        # Sweet and acidic taste, apple-like smell: apple
                        elif sweetness == "high" and acidity == "high" and apple_smell:
                            return "apple"
                        else:
                            return "Unknown fruit"

    # Default case
    return "Unknown fruit"