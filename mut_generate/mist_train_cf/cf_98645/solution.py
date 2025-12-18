"""
QUESTION:
Create a Python function called `calculate_bmr`, `calculate_daily_calorie_needs`, and `calculate_daily_calorie_deficit_or_surplus` to calculate the basal metabolic rate (BMR) using the Harris-Benedict formula and daily calorie needs based on the BMR, activity level, and thermic effect of food (TEF). 

The Harris-Benedict formula for males is: BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) - (5.677 x age in years). The formula for females is: BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) - (4.330 x age in years). 

The TEF is estimated to be around 10% of daily calorie intake. The daily calorie needs should be calculated as BMR x activity level x TEF. The function `calculate_daily_calorie_deficit_or_surplus` should take daily calorie needs and daily calorie intake as input and return the daily calorie deficit or surplus.

The input parameters for the functions are gender, weight, height, age, activity level, and daily calorie intake. The output should be the calculated BMR, daily calorie needs, and daily calorie deficit or surplus.
"""

# calculate BMR using Harris-Benedict formula
def calculate_bmr(gender, weight, height, age):
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

# calculate daily calorie needs based on BMR, activity level, and TEF
def calculate_daily_calorie_needs(gender, weight, height, age, activity_level):
    bmr = calculate_bmr(gender, weight, height, age)
    tef = 0.10  # thermic effect of food
    daily_calorie_needs = bmr * activity_level * (1 + tef)
    return daily_calorie_needs

# calculate daily calorie deficit or surplus
def calculate_daily_calorie_deficit_or_surplus(gender, weight, height, age, activity_level, daily_calorie_intake):
    daily_calorie_needs = calculate_daily_calorie_needs(gender, weight, height, age, activity_level)
    daily_calorie_deficit_or_surplus = daily_calorie_intake - daily_calorie_needs
    return daily_calorie_deficit_or_surplus