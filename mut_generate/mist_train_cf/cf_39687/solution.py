"""
QUESTION:
Determine the next action of an AI agent based on the state of its animator and a finite state machine (FSM). Implement a function named `determine_next_action` that takes the current state of the animator, the value of `is_human_exists`, and the current state of the FSM as inputs. The function should return a string representing the next action the AI agent should take.

The next action should be determined by the following conditions:
- If the current animator state is "Wait" and `is_human_exists` is true, the next action should be "Transition to State_Contact_Dragon".
- If `is_human_exists` is false, the next action should be "Set Is_Sleep to true".
- If none of the conditions are met, the next action should be "No action needed".

The function signature should be `def determine_next_action(animator_state: str, is_human_exists: bool, fsm_state: str) -> str:`
"""

def determine_next_action(animator_state: str, is_human_exists: bool, fsm_state: str) -> str:
    if animator_state == "Wait" and is_human_exists:
        return "Transition to State_Contact_Dragon"
    elif not is_human_exists:
        return "Set Is_Sleep to true"
    else:
        return "No action needed"