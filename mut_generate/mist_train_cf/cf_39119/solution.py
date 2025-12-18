"""
QUESTION:
Write a function `process_actions(owner, blocking_actor)` that takes two parameters:
- `owner`: A dictionary representing the owner of the action with a "tag" key containing a list of tags associated with the owner.
- `blocking_actor`: A dictionary representing the blocking actor with a "tag" key containing a list of tags associated with the blocking actor.

The function should return a list of actions to be performed based on the game logic. If there is no blocking actor, the function should return a list containing a walk action. If there is a blocking actor tagged as an enemy, the function should return a list containing an attack action if the owner is tagged as a player, or a list containing a delay action if the owner is not tagged as a player. Each action should be represented as a dictionary with an "action_type" key.
"""

def entance(owner, blocking_actor):
    result = []
    if not blocking_actor:
        result.append({"action_type": "walk"})
    elif "enemy" in blocking_actor["tag"]:
        if "player" in owner["tag"]:
            result.append({"action_type": "attack"})
        else:
            result.append({"action_type": "delay"})
    return result