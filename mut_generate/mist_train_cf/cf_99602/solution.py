"""
QUESTION:
Write a function `calculate_sleep_hours` that takes three parameters: `age`, `gender`, and `activity_level`. The function should return the recommended hours of sleep per night for an adult based on their age, gender, and activity level. The age range is between 18 and 64. The `gender` parameter should be either 'male' or 'female', and the `activity_level` parameter should be either 'sedentary', 'moderate', or 'active'. The function should return a float value representing the recommended hours of sleep per night.
"""

def calculate_sleep_hours(age, gender, activity_level):
    if gender == 'male':
        if age >= 18 and age <= 25:
            if activity_level == 'sedentary':
                return 8
            elif activity_level == 'moderate':
                return 8.5
            elif activity_level == 'active':
                return 9
        elif age >= 26 and age <= 64:
            if activity_level == 'sedentary':
                return 7.5
            elif activity_level == 'moderate':
                return 8
            elif activity_level == 'active':
                return 8.5
    elif gender == 'female':
        if age >= 18 and age <= 25:
            if activity_level == 'sedentary':
                return 8.5
            elif activity_level == 'moderate':
                return 9
            elif activity_level == 'active':
                return 9.5
        elif age >= 26 and age <= 64:
            if activity_level == 'sedentary':
                return 8
            elif activity_level == 'moderate':
                return 8.5
            elif activity_level == 'active':
                return 9