"""
QUESTION:
Create a function named `merge_activities` that takes two JSON objects as arguments. Each JSON object contains user activities with keys as "userID" and respective sets of activity IDs stored as values. The function should merge these two datasets without creating duplicates and return a merged version in a new JSON object. 

The function should be able to handle edge cases such as handling duplicate activities across different users and having one or both JSON objects being empty. The output should have the same structure as the input JSON objects, with a single key named "userActivities" that contains the merged user activities.
"""

def merge_activities(json1, json2):
    result = {}
    all_users = set(list(json1.keys()) + list(json2.keys()))
    
    for user in all_users:
        activities = set()
        if user in json1:
            activities.update(json1[user])
            
        if user in json2:
            activities.update(json2[user])
            
        result[user] = activities
        
    return {"userActivities": result}