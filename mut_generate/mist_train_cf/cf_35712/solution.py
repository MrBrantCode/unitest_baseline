"""
QUESTION:
Implement a function `track_episodes(episode_list)` that takes a list of episode strings in the format "SxEx" as input, where 'S' represents the season number and 'E' represents the episode number, and returns a dictionary where the keys are the season numbers and the values are lists of episode numbers for each season.
"""

import re

def track_episodes(episode_list):
    processed_dict = {}
    for episode_str in episode_list:
        season_match = re.match(r"S(\d+)E\d+", episode_str)
        episode_match = re.match(r"S\d+E(\d+)", episode_str)
        if season_match:
            season = season_match.group(1)
            if episode_match:
                episode = int(episode_match.group(1))
                if season in processed_dict:
                    processed_dict[season].append(episode)
                else:
                    processed_dict[season] = [episode]
    return processed_dict