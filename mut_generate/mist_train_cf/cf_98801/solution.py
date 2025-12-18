"""
QUESTION:
Create a program with three functions: `get_user_inputs`, `calc_success_rate`, and `main`. The `get_user_inputs` function should prompt the user for team skills (integer between 1 and 10), resource level (integer between 1 and 10), and risk level (float between 0 and 1). The `calc_success_rate` function should take the user inputs and three weights (floats between 0 and 1 that sum to 1) as arguments, and return a success rate calculated as the weighted average of the inputs. The `main` function should call `get_user_inputs`, prompt the user for weights, call `calc_success_rate`, and print the success rate as a percentage.
"""

def entrance(team_skills, resource_level, risk_level, team_weight, resource_weight, risk_weight):
    # Calculate weighted average of team skills, resource level, and risk level
    weighted_team = team_skills * team_weight
    weighted_resource = resource_level * resource_weight
    weighted_risk = risk_level * risk_weight
    total_weight = team_weight + resource_weight + risk_weight
    
    # Compute success rate
    success_rate = (weighted_team + weighted_resource + weighted_risk) / total_weight
    
    return success_rate