"""
QUESTION:
Create a function `find_activity` that takes a list of activities and an intensity level as input. The function should return a list of activities that match the given intensity level and have a duration of less than 30 minutes. The intensity levels and their corresponding activities are as follows: 
- Low: Yoga, Reading books
- Moderate: Dancing, Running 
- High: Swimming
- Very high: Basketball 
The duration of each activity is assumed to be within the 30-minute limit for the corresponding intensity level.
"""

def find_activity(activity_list, intensity_level):
    activities = []
    intensity_dict = {
        "Low": ["Yoga", "Reading books"],
        "Moderate": ["Dancing", "Running"],
        "High": ["Swimming"],
        "Very high": ["Basketball"]
    }
    for activity in activity_list:
        if activity in intensity_dict.get(intensity_level, []):
            activities.append(activity)
    return activities