"""
QUESTION:
Implement a function named `calculate_demand_profile` that calculates a daily demand profile based on hourly demand weights and time periods. The function takes in three parameters: `daily_hours`, a list of integers representing the hours in a day (0 to 23); `hourly_demand`, a dictionary where the keys are strings representing time periods ('AM', 'Inter peak', 'PM', 'Night') and the values are integers representing the hourly demand for each period; and `times`, a dictionary where the keys are tuples of start and end hours for each time period, and the values are integers representing the period type (0 for 'AM', 1 for 'Inter peak', 2 for 'PM', 3 for 'Night'). The function returns a list of integers representing the demand profile for each hour of the day.
"""

from typing import List, Dict, Tuple

def calculate_demand_profile(daily_hours: List[int], hourly_demand: Dict[str, int], times: Dict[Tuple[int, int], int]) -> List[int]:
    demand_profile = [0] * 24  # Initialize demand profile for each hour

    for hour in daily_hours:
        for (start, end), period in times.items():
            if end > hour >= start:
                weight = hourly_demand[list(hourly_demand.keys())[period]]  # Get the hourly demand weight for the corresponding period
                demand_profile[hour] = weight  # Set the demand for the current hour based on the period weight

    return demand_profile