"""
QUESTION:
Implement the `getRelocations` function that takes `GVT`, `activities`, and `horizon` as parameters and returns a dictionary of relocations for the activities. 

The function should include an activity in the relocations dictionary if its model's location is different from the relocation location and the model is relocatable. If no activities meet the relocation criteria, the function should set the `run_GVT` attribute of the system's state to 1.0.
"""

def getRelocations(GVT, activities, horizon, state, model_ids, relocator):
    """
    This function generates a dictionary of relocations for the activities based on their models' locations and relocatability.

    Args:
    GVT (float): The global virtual time.
    activities (dict): A dictionary of activities.
    horizon (float): The time horizon.
    state (object): The system's state.
    model_ids (dict): A dictionary of model IDs.
    relocator (object): The relocator object.

    Returns:
    dict: A dictionary of relocations for the activities.
    """
    relocations = {}
    for key in activities:
        if model_ids[key].location != relocator.getRelocations[key] and model_ids[key].relocatable:
            relocations[key] = relocator.getRelocations[key]
    if not relocations:
        state.run_GVT = 1.0
    return relocations