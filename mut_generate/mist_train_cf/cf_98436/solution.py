"""
QUESTION:
Create a function named `calculate_caloric_intake` that calculates the daily caloric intake for an individual based on their age, weight, height, gender, activity level, and weight loss goal. The formula for calculating the caloric intake is provided as follows: 
Caloric Intake = BMR x Activity Factor x Weight Loss Factor
BMR = 10 x weight (kg) + 6.25 x height (cm) - 5 x age (years) + 5 (for men)
BMR = 10 x weight (kg) + 6.25 x height (cm) - 5 x age (years) - 161 (for women)
Activity Factor: 
1.2 = Sedentary (little or no exercise)
1.375 = Lightly active (light exercise or sports 1-3 days a week)
1.55 = Moderately active (moderate exercise or sports 3-5 days a week)
1.725 = Very active (hard exercise or sports 6-7 days a week)
1.9 = Extremely active (very hard exercise or sports, physical job or training twice a day)
Weight Loss Factor:
1 = No weight loss
0.85 = 0.5 kg per week weight loss
0.8 = 1 kg per week weight loss
0.75 = 1.5 kg per week weight loss
0.7 = 2 kg per week weight loss.
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