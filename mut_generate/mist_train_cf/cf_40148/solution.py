"""
QUESTION:
The function `calculate_total_calories` should take a string containing nutritional information for one or more food items as input. Each food item is represented in the format "name fat/protein/carbohydrates kcal", where the macronutrient values are given in grams and kcal is the calorie value. The function should calculate the total calories for all the food items in the input string based on the macronutrient values (fat * 9 + protein * 4 + carbohydrates * 4) and the given calorie value, and return the sum of the calories. The input string will always be non-empty and well-formatted, and the macronutrient values and calorie value are all non-negative integers.
"""

def entrance(nutritional_info: str) -> int:
    total_calories = 0
    items = nutritional_info.split(';')  
    for item in items:
        parts = item.split()  
        macronutrients = parts[1].split('/')  
        calories = int(parts[2])  
        total_calories += (int(macronutrients[0]) * 9 + int(macronutrients[1]) * 4 + int(macronutrients[2]) * 4)
    return total_calories