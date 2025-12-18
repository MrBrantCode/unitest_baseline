"""
QUESTION:
Create a function `calculate_sleep_hours` that takes three parameters: `age`, `gender`, and `activity_level`. The function should return the recommended hours of sleep per night for an adult based on the following conditions: 
- age is between 18 and 64
- gender is either 'male' or 'female'
- activity_level is 'sedentary', 'moderate', or 'active'
- recommended hours of sleep vary based on a combination of age, gender, and activity level as shown in the table below:
  - male: 
    - 18-25: sedentary (8), moderate (8.5), active (9)
    - 26-64: sedentary (7.5), moderate (8), active (8.5)
  - female:
    - 18-25: sedentary (8.5), moderate (9), active (9.5)
    - 26-64: sedentary (8), moderate (8.5), active (9)
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