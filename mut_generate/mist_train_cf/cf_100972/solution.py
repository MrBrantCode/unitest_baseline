"""
QUESTION:
Create a function called `calculate_bmr` that calculates the Basal Metabolic Rate (BMR) using the Harris-Benedict formula. The function should take four parameters: `gender`, `weight`, `height`, and `age`. The formula for males is BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) - (5.677 x age in years), and for females is BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) - (4.330 x age in years). Additionally, create two other functions `calculate_daily_calorie_needs` and `calculate_daily_calorie_deficit_or_surplus` to calculate the daily calorie needs and daily calorie deficit or surplus respectively, based on the calculated BMR. Assume the thermic effect of food (TEF) is 10% of the daily calorie intake.
"""

# calculate BMR using Harris-Benedict formula
def calculate_bmr(gender, weight, height, age):
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

# calculate daily calorie needs based on BMR, activity level, and TEF
def calculate_daily_calorie_needs(bmr, activity_level):
    tef = 0.10 # thermic effect of food
    daily_calorie_needs = bmr * activity_level * (1 + tef)
    return daily_calorie_needs

# calculate daily calorie deficit or surplus
def calculate_daily_calorie_deficit_or_surplus(daily_calorie_needs, daily_calorie_intake):
    daily_calorie_deficit_or_surplus = daily_calorie_intake - daily_calorie_needs
    return daily_calorie_deficit_or_surplus