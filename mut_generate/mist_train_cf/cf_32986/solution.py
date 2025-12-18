"""
QUESTION:
Create a function `calculate_bmi_category` that takes in two parameters: `weight` (in kg) and `height` (in meters), and returns the BMI category as a string. The BMI category is determined by the following ranges: 
- "Underweight" if BMI is less than 18
- "Normal" if BMI is between 18 and 25 (inclusive)
- "Overweight" if BMI is 25 or greater. The BMI is calculated as weight (kg) / (height (m) * height (m)).
"""

def calculate_bmi_category(weight, height):
    bmi = weight / (height * height)
    if bmi < 18:
        return "Underweight"
    elif 18 <= bmi <= 25:
        return "Normal"
    else:
        return "Overweight"