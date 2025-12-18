"""
QUESTION:
Create a function named `calculate_caloric_intake` that calculates the caloric intake based on the provided formula. The function should take in the following parameters: age, weight, height, gender, activity level, and weight loss goal. The activity levels are 'sedentary', 'lightly active', 'moderately active', 'very active', and 'extremely active'. The weight loss goals are 'none', '0.5 kg per week', '1 kg per week', '1.5 kg per week', and '2 kg per week'. The function should return the calculated caloric intake.
"""

def calculate_caloric_intake(age, weight, height, gender, activity_level, weight_loss_goal):
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    activity_factor = {'sedentary': 1.2, 'lightly active': 1.375, 'moderately active': 1.55, 'very active': 1.725, 'extremely active': 1.9}
    weight_loss_factor = {'none': 1, '0.5 kg per week': 0.85, '1 kg per week': 0.8, '1.5 kg per week': 0.75, '2 kg per week': 0.7}
    caloric_intake = bmr * activity_factor[activity_level] * weight_loss_factor[weight_loss_goal]
    return caloric_intake