"""
QUESTION:
###BACKGROUND:
Jacob recently decided to get healthy and lose some weight. He did a lot of reading and research and after focusing on steady exercise and a healthy diet for several months, was able to shed over 50 pounds! Now he wants to share his success, and has decided to tell his friends and family how much weight they could expect to lose if they used the same plan he followed.

Lots of people are really excited about Jacob's program and they want to know how much weight they would lose if they followed his plan. Unfortunately, he's really bad at math, so he's turned to you to help write a program that will calculate the expected weight loss for a particular person, given their weight and how long they think they want to continue the plan.

###TECHNICAL DETAILS:
Jacob's weight loss protocol, if followed closely, yields loss according to a simple formulae, depending on gender. Men can expect to lose 1.5% of their current body weight each week they stay on plan. Women can expect to lose 1.2%. (Children are advised to eat whatever they want, and make sure to play outside as much as they can!)

###TASK:
Write a function that takes as input:
```
- The person's gender ('M' or 'F');
- Their current weight (in pounds);
- How long they want to stay true to the protocol (in weeks);
```
and then returns the expected weight at the end of the program.

###NOTES:
Weights (both input and output) should be decimals, rounded to the nearest tenth.
Duration (input) should be a whole number (integer). If it is not, the function should round to the nearest whole number.
When doing input parameter validity checks, evaluate them in order or your code will not pass final tests.
"""

def calculate_expected_weight_loss(gender, weight, duration):
    """
    Calculate the expected weight loss for a person following Jacob's weight loss protocol.

    Parameters:
    - gender (str): The gender of the person, either 'M' for male or 'F' for female.
    - weight (float): The current weight of the person in pounds.
    - duration (int): The number of weeks the person plans to stay on the protocol.

    Returns:
    - float: The expected weight at the end of the protocol, rounded to the nearest tenth.
    - str: 'Invalid gender' if the gender is not 'M' or 'F'.
    - str: 'Invalid weight' if the weight is less than or equal to 0.
    - str: 'Invalid duration' if the duration is less than or equal to 0.
    """
    # Validate gender
    if gender not in ['M', 'F']:
        return 'Invalid gender'
    
    # Validate weight
    if weight <= 0:
        return 'Invalid weight'
    
    # Validate duration and round it to the nearest whole number
    duration = round(duration)
    if duration <= 0:
        return 'Invalid duration'
    
    # Determine the weight loss factor based on gender
    weight_loss_factor = 0.985 if gender == 'M' else 0.988
    
    # Calculate the expected weight after the given duration
    for _ in range(duration):
        weight *= weight_loss_factor
    
    # Return the expected weight rounded to the nearest tenth
    return round(weight, 1)