"""
QUESTION:
Create a function `ShowerHead` that takes into account multiple factors to determine the overall performance of a shower head. The function should consider the following attributes: brand, price, ease of installation, water efficiency, user experience, compatibility with different types of water pressure, user preferences for water flow and temperature, durability over time, resistance to potential damage from hard water, and customer satisfaction rating. The function should assign weights to each attribute based on its importance and calculate the overall performance score by summing up the weighted scores for each attribute. The function should return the overall performance score.

The input parameters should include:

- `brand`: string
- `price`: float
- `ease_of_installation`: float
- `water_efficiency`: float
- `user_experience`: float
- `water_pressure_compatibility`: integer
- `water_flow_temperature_preferences`: string
- `durability_over_time`: integer
- `resistance_to_hard_water_damage`: string
- `customer_satisfaction_rating`: float

The output should be the overall performance score of the shower head, calculated based on the weighted scores of the input attributes.
"""

def ShowerHead(brand, price, ease_of_installation, water_efficiency, user_experience, water_pressure_compatibility, water_flow_temperature_preferences, durability_over_time, resistance_to_hard_water_damage, customer_satisfaction_rating):
    # weights for each attribute
    price_weight = 0.2
    installation_weight = 0.1
    efficiency_weight = 0.1
    experience_weight = 0.1
    pressure_weight = 0.1
    preferences_weight = 0.1
    durability_weight = 0.15
    resistance_weight = 0.1
    satisfaction_weight = 0.05

    # calculate weighted score for each attribute
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

    # calculate overall performance score
    overall_score = sum([price_score, installation_score, efficiency_score, experience_score, pressure_score, preferences_score, durability_score, resistance_score, satisfaction_score])
    return overall_score