"""
QUESTION:
Create a function `recommended_sleep_hours` that takes in two parameters: `age` and `gender`. The function should return the recommended hours of sleep per night based on the guidelines from the National Sleep Foundation. The guidelines are as follows: 
- Infants (0-12 months): 14-17 hours
- Toddlers (1-2 years): 11-14 hours
- Preschoolers (3-5 years): 10-13 hours
- School-age children (6-13 years): 9-11 hours
- Teenagers (14-17 years): 8-10 hours
- Young adults (18-64 years): 7-9 hours
- Older adults (65 years and over): 7-8 hours
The function should return 'Invalid gender input' if the gender is not 'male' or 'female'.
"""

def recommended_sleep_hours(age, gender):
    if gender not in ['male', 'female']:
        return 'Invalid gender input'
    
    if age >= 65:
        return '7-8 hours'
    elif age >= 18:
        return '7-9 hours'
    elif age >= 14:
        return '8-10 hours'
    elif age >= 6:
        return '9-11 hours'
    elif age >= 3:
        return '10-13 hours'
    elif age >= 1:
        return '11-14 hours'
    else:
        return '14-17 hours'