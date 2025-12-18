"""
QUESTION:
Create a function named `count_actions` that takes a list of dictionaries as input where each dictionary represents an agent and contains a key "actions" with a list of actions as its value. The function should return a dictionary where the keys are the actions and the values are their corresponding frequencies across all agents. The function should handle duplicate actions for each agent.
"""

def count_actions(agents):
    action_frequency = {}
    for agent in agents:
        for action in agent["actions"]:
            action_frequency[action] = action_frequency.get(action, 0) + 1
    return action_frequency