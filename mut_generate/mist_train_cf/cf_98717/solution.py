"""
QUESTION:
Create a function `compare_nutrient_density` that takes in two dictionaries, each representing the nutrient composition of a fruit, with keys 'Calories', 'Protein', 'Fat', and 'Carbohydrate'. The function should calculate and return the nutrient density of each fruit by dividing the total nutrient content by the total energy content (calories), and compare the nutrient composition of the two fruits.
"""

def compare_nutrient_density(fruit1, fruit2):
    """
    Calculate and compare the nutrient density of two fruits.

    Args:
        fruit1 (dict): Nutrient composition of the first fruit.
        fruit2 (dict): Nutrient composition of the second fruit.

    Returns:
        dict: A dictionary containing the nutrient density of each fruit.
    """
    # Calculate the total nutrient content of each fruit
    total_nutrient_fruit1 = fruit1['Protein'] + fruit1['Fat'] + fruit1['Carbohydrate']
    total_nutrient_fruit2 = fruit2['Protein'] + fruit2['Fat'] + fruit2['Carbohydrate']

    # Calculate the nutrient density of each fruit
    nutrient_density_fruit1 = total_nutrient_fruit1 / fruit1['Calories']
    nutrient_density_fruit2 = total_nutrient_fruit2 / fruit2['Calories']

    # Return the nutrient density of each fruit
    return {
        'Fruit 1': nutrient_density_fruit1,
        'Fruit 2': nutrient_density_fruit2
    }