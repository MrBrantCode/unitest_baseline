"""
QUESTION:
Develop a program with functions `bmi_calculator`, `whr_calculator`, `bmr_calculator`, and `mhr_calculator`. 

- `bmi_calculator` calculates the body mass index (BMI) given weight and height.
- `whr_calculator` calculates the waist-to-hip ratio (WHR) given waist and hip circumference.
- `bmr_calculator` estimates basal metabolic rate (BMR) using the Katch-McArdle formula, which takes into account the person's lean body mass (LBM), body fat percentage, age, gender, and activity level.
- `mhr_calculator` predicts maximum heart rate (MHR) using the Tanaka equation, based on age and sex.
"""

def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def whr_calculator(waist, hip):
    whr = waist / hip
    return whr

def bmr_calculator(weight, height, age, gender, body_fat, activity_level):
    LBM = weight * (1 - body_fat)
    if gender == "male":
        bmr = 370 + (21.6 * LBM) + (6.2 * weight) - (4.7 * age)
    elif gender == "female":
        bmr = 370 + (21.6 * LBM) + (6.2 * weight) - (4.7 * age) - 64
    else:
        return "Invalid gender"
    if activity_level == 1:
        bmr *= 1.2
    elif activity_level == 2:
        bmr *= 1.375
    elif activity_level == 3:
        bmr *= 1.55
    elif activity_level == 4:
        bmr *= 1.725
    elif activity_level == 5:
        bmr *= 1.9
    else:
        return "Invalid activity level"
    return bmr

def mhr_calculator(age, gender):
    if gender == "male":
        mhr = 208 - (0.7 * age)
    elif gender == "female":
        mhr = 206 - (0.88 * age)
    else:
        return "Invalid gender"
    return mhr