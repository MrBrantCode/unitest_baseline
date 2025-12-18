"""
QUESTION:
Create a function `agent_movement(input_command, flag, environment)` that takes in an input command ("w" for up, "a" for left, "s" for down, "d" for right), an integer flag value, and an environment object with methods `step(action)` and `reset()`. The function should return a tuple `(action, observation, reward, done)` representing the agent's action, the resulting observation from the environment, the reward received, and a boolean indicating if the episode is done after the agent's action. If `flag` is less than 0, the agent should take a specific action.
"""

def agent_movement(input_command, flag, environment):
    action = [0, 0]  

    if input_command == "w":
        action[1] = 1  
    elif input_command == "a":
        action[0] = -1  
    elif input_command == "s":
        action[1] = -1  
    elif input_command == "d":
        action[0] = 1  

    if flag < 0:
        action[0] = -0.1  

    observation, reward, done, _ = environment.step(action)  

    return action, observation, reward, done