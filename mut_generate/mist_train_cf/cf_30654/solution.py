"""
QUESTION:
Implement the `determine_objective_state` method in the `MissionObjectiveData` class. The method should return the state of the mission objective based on the following conditions and tunable parameters:

- `completes_mission`: a boolean indicating if completion of the objective completes the mission
- `requires_previous_objective_complete`: a boolean indicating if the objective requires the previous objective to be complete
- `object_state_changes_on_active`: a boolean indicating if the tuned state changes when the objective is active
- `object_state_changes_on_complete`: a boolean indicating if the tuned state changes when the objective is complete
- `objective_state`: the current state of the objective
- `previous_objective_complete`: a boolean indicating if the previous objective is complete
- `MISSION_OBJECTIVE_COMPLETE`, `MISSION_OBJECTIVE_ACTIVE`, `MISSION_OBJECTIVE_NOT_ACTIVE` constants

The method should follow these rules:
- If `completes_mission` is true and the objective is complete, return `MISSION_OBJECTIVE_COMPLETE`.
- If `requires_previous_objective_complete` is true and the previous objective is not complete, return `MISSION_OBJECTIVE_NOT_ACTIVE`.
- If `object_state_changes_on_active` is enabled, apply the tuned state changes when the objective is active and able to be completed.
- If `object_state_changes_on_complete` is enabled, apply the tuned state changes when the objective is complete.
- If none of the above conditions apply, return `MISSION_OBJECTIVE_ACTIVE` if the objective is active, and `MISSION_OBJECTIVE_NOT_ACTIVE` if it is not.
"""

def determine_objective_state(completes_mission, requires_previous_objective_complete, object_state_changes_on_active, object_state_changes_on_complete, objective_state, previous_objective_complete, MISSION_OBJECTIVE_COMPLETE, MISSION_OBJECTIVE_ACTIVE, MISSION_OBJECTIVE_NOT_ACTIVE):
    if completes_mission and objective_state == MISSION_OBJECTIVE_COMPLETE:
        return MISSION_OBJECTIVE_COMPLETE
    elif requires_previous_objective_complete and not previous_objective_complete:
        return MISSION_OBJECTIVE_NOT_ACTIVE
    else:
        if object_state_changes_on_active and objective_state == MISSION_OBJECTIVE_ACTIVE:
            pass
        if object_state_changes_on_complete and objective_state == MISSION_OBJECTIVE_COMPLETE:
            pass
        return MISSION_OBJECTIVE_ACTIVE if objective_state == MISSION_OBJECTIVE_ACTIVE else MISSION_OBJECTIVE_NOT_ACTIVE