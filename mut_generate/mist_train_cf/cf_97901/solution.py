"""
QUESTION:
Create a function `race_preparation` that takes in the following parameters: `race_date`, `race_location`, `race_distance`, `athlete_diet`, `athlete_training_regimen`, and `athlete_equipment`. The function should return a string that provides the athlete's preparation plan for the race, formatted with bullet points for each piece of information.
"""

def race_preparation(race_date, race_location, race_distance, athlete_diet, athlete_training_regimen, athlete_equipment):
    return f"To prepare for the {race_distance} race in {race_location} on {race_date}, the athlete should:\n• consume a {athlete_diet} diet leading up to the race\n• follow a {athlete_training_regimen} program\n• wear {athlete_equipment} for optimal performance."