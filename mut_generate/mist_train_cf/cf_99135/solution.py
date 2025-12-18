"""
QUESTION:
Create a Python function `find_activity(activity_list, intensity_level)` that takes a list of activities and an intensity level as input. The function should return a list of activities that match the given intensity level and have a duration of less than 30 minutes. The intensity levels and their corresponding activities are: 
- Low: Yoga, Reading books
- Moderate: Dancing
- High: Swimming, Running
- Very high: Basketball 

Note that the intensity levels and activities are fixed and should be hardcoded in the function. The function should return an empty list if no activities match the given intensity level.
"""

def find_activity(activity_list, intensity_level):
    activities = []
    intensity_dict = {
        "Low": ["Yoga", "Reading books"],
        "Moderate": ["Dancing"],
        "High": ["Swimming", "Running"],
        "Very high": ["Basketball"]
    }
    
    for activity in activity_list:
        if activity in intensity_dict.get(intensity_level, []):
            activities.append(activity)
            
    return activities