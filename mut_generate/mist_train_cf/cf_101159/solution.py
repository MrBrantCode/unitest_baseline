"""
QUESTION:
Create a function called `ShowerHead` that takes the following parameters: brand, price, ease of installation, water efficiency, user experience, water pressure compatibility, water flow and temperature preferences, durability over time, resistance to potential damage from hard water, and customer satisfaction rating. The function should calculate the overall performance score of the shower head based on these parameters. Each parameter should be weighted based on its importance. The function should return the overall performance score. 

Note that the weights for each attribute should be as follows: price (0.2), ease of installation (0.1), water efficiency (0.1), user experience (0.1), water pressure compatibility (0.1), water flow and temperature preferences (0.1), durability over time (0.15), resistance to potential damage from hard water (0.1), and customer satisfaction rating (0.05). 

Additionally, the function should evaluate the water flow and temperature preferences attribute as 1 if it is 'Customizable' and 0 otherwise, and the resistance to potential damage from hard water attribute as 1 if it is 'Yes' and 0 otherwise.
"""

def ShowerHead(brand, price, ease_of_installation, water_efficiency, user_experience, water_pressure_compatibility, water_flow_temperature_preferences, durability_over_time, resistance_to_hard_water_damage, customer_satisfaction_rating):
    price_weight = 0.2
    installation_weight = 0.1
    efficiency_weight = 0.1
    experience_weight = 0.1
    pressure_weight = 0.1
    preferences_weight = 0.1
    durability_weight = 0.15
    resistance_weight = 0.1
    satisfaction_weight = 0.05
    
    price_score = 1 / price * price_weight
    installation_score = ease_of_installation * installation_weight
    efficiency_score = water_efficiency * efficiency_weight
    experience_score = user_experience * experience_weight
    pressure_score = water_pressure_compatibility * pressure_weight
    preferences_score = 1 if water_flow_temperature_preferences == 'Customizable' else 0
    preferences_score *= preferences_weight
    durability_score = durability_over_time * durability_weight
    resistance_score = 1 if resistance_to_hard_water_damage == 'Yes' else 0
    resistance_score *= resistance_weight
    satisfaction_score = customer_satisfaction_rating / 10 * satisfaction_weight
    
    overall_score = sum([price_score, installation_score, efficiency_score, experience_score, pressure_score, preferences_score, durability_score, resistance_score, satisfaction_score])
    return overall_score