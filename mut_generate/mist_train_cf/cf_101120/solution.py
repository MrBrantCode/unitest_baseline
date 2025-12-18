"""
QUESTION:
Write a function `calc_success_rate` that takes in user inputs for team skills (1-10), resource level (1-10), risk level (0-1), weight for team skills (0-1), weight for resource level (0-1), and weight for risk level (0-1), and calculates the success rate using weighted averages. The weights must sum to 1. The function should handle invalid inputs and ensure that all inputs are within their specified ranges.
"""

def calc_success_rate(team_skills, resource_level, risk_level, team_weight, resource_weight, risk_weight):
    # Calculate weighted average of team skills, resource level, and risk level
    weighted_team = team_skills * team_weight
    weighted_resource = resource_level * resource_weight
    weighted_risk = risk_level * risk_weight
    total_weight = team_weight + resource_weight + risk_weight

    # Compute success rate
    success_rate = (weighted_team + weighted_resource + weighted_risk) / total_weight

    return success_rate