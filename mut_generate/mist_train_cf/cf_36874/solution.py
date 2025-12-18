"""
QUESTION:
Implement a function `choose_action(key, context, actions)` that selects the most suitable action based on the provided key and context. The function should take three parameters:
- `key`: A string representing the key identifying the interaction.
- `context`: A dictionary containing information about the current game context. (This parameter is not used in the given solution and may be ignored)
- `actions`: A list of available actions to choose from, where each action is an object with attributes such as `damage` and `exploration_value`.

The function should return the most suitable action based on the provided key and context. It can be assumed that the `actions` list is non-empty.
"""

def choose_action(key, context, actions):
    if key == "combat":
        return max(actions, key=lambda action: action.damage)
    elif key == "exploration":
        return max(actions, key=lambda action: action.exploration_value)
    else:
        return actions[0]