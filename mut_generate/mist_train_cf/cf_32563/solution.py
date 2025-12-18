"""
QUESTION:
Implement a function `play_game` that utilizes a reinforcement learning environment `venv` and a pre-trained model `model` to play a game for a specified number of episodes `num_episodes`. The function should return the total rewards obtained across all episodes. The function should reset the environment at the start of each episode, use the model to predict actions, and step through the environment to obtain rewards. The environment and model are expected to have `reset`, `step`, and `predict` methods, respectively.
"""

def play_game(venv, model, num_episodes):
    total_rewards = 0
    for _ in range(num_episodes):
        obs = venv.reset()
        episode_reward = 0
        done = False
        while not done:
            action, _states = model.predict(obs, deterministic=True)
            obs, reward, done, _ = venv.step(action)
            episode_reward += reward
        total_rewards += episode_reward
    return total_rewards