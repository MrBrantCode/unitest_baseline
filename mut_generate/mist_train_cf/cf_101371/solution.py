"""
QUESTION:
Write a function named `calculate_nutrient_content` that takes two lists as input, `ingredients` and `serving_sizes`, and returns a dictionary containing the total nutrient content of a meal based on the ingredients and their corresponding serving sizes. The `nutrient_values` dictionary provides the nutrient values per serving for each ingredient.
"""

def calculate_nutrient_content(ingredients, serving_sizes):
    nutrient_values = {
        'carbs': 25,
        'protein': 10,
        'fat': 5,
        'vitamin_a': 100,
        'vitamin_c': 20,
        'calcium': 150,
        'iron': 2
    }
    total_nutrients = {}
    for i, ingredient in enumerate(ingredients):
        for nutrient, value in nutrient_values.items():
            if nutrient in ingredient:
                if nutrient not in total_nutrients:
                    total_nutrients[nutrient] = 0
                total_nutrients[nutrient] += value * serving_sizes[i]
    return total_nutrients