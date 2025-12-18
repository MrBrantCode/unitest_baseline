"""
QUESTION:
Implement a function `average_review_score_for_company_rating_one` that takes an array of vehicle objects and returns the average review scores rating for vehicles with a company rating of 1. Each vehicle object has properties: "engines", "passenger_capacity", "crew", "company_rating", and "review_scores_rating". The function should return a single floating-point number, rounded to two decimal places. If there are no vehicles with a company rating of 1, return 0.
"""

from typing import List, Dict, Union

def average_review_score_for_company_rating_one(vehicles: List[Dict[str, Union[int, float]]]) -> float:
    company_rating_one_vehicles = [vehicle["review_scores_rating"] for vehicle in vehicles if vehicle["company_rating"] == 1]
    if not company_rating_one_vehicles:
        return 0
    average_rating = sum(company_rating_one_vehicles) / len(company_rating_one_vehicles)
    return round(average_rating, 2)