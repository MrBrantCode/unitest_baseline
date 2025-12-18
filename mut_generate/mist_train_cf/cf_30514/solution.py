"""
QUESTION:
Create a function `determine_next_activity(pipeline, eg_id, act_executed_id)` that takes in a pipeline dictionary `pipeline`, an exclusive gateway ID `eg_id`, and an executed activity ID `act_executed_id`, and returns the ID of the next activity to be executed. The `pipeline` dictionary contains a list of activities and their relationships. Each activity in the `pipeline` has an "incoming" key representing the activities that come before it and an "exclusive_gateway" key representing the ID of the exclusive gateway that it belongs to. The function should analyze the pipeline structure and the executed activity to determine the next step in the workflow.
"""

def determine_next_activity(pipeline, eg_id, act_executed_id):
    activities = pipeline["activities"]
    incoming_relationships = {}
    for activity_id, activity_data in activities.items():
        incoming_relationships[activity_id] = activity_data.get("incoming", [])

    next_activity_id = None
    for activity_id, activity_data in activities.items():
        if act_executed_id in incoming_relationships[activity_id]:
            if "exclusive_gateway" in activity_data and activity_data["exclusive_gateway"] == eg_id:
                next_activity_id = activity_id
                break

    return next_activity_id