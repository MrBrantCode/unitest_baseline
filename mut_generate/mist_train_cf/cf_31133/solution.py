"""
QUESTION:
Implement a function `process_game_objects` that takes a dictionary `game_objects` as input, where the dictionary has two keys: "spawns" and "towers". Each key maps to a list of objects, with each object being a dictionary containing "name", "type", and "position" keys. The "position" key maps to a tuple containing the x and y coordinates of the object. 

The function should return a new dictionary containing the count of each type of object ("spawns" and "towers") and the average position for each type. The average position should be calculated separately for "spawns" and "towers" based on the x and y coordinates of the objects of each type.

Restrictions: The input dictionary is guaranteed to have the "spawns" and "towers" keys, and each object in the lists has the "name", "type", and "position" keys. The "position" value is a tuple with two elements.
"""

def process_game_objects(game_objects):
    spawn_count = len(game_objects["spawns"])
    tower_count = len(game_objects["towers"])

    spawn_total_x = sum(obj["position"][0] for obj in game_objects["spawns"])
    spawn_total_y = sum(obj["position"][1] for obj in game_objects["spawns"])
    tower_total_x = sum(obj["position"][0] for obj in game_objects["towers"])
    tower_total_y = sum(obj["position"][1] for obj in game_objects["towers"])

    spawn_avg_x = spawn_total_x / spawn_count if spawn_count > 0 else 0
    spawn_avg_y = spawn_total_y / spawn_count if spawn_count > 0 else 0
    tower_avg_x = tower_total_x / tower_count if tower_count > 0 else 0
    tower_avg_y = tower_total_y / tower_count if tower_count > 0 else 0

    return {
        "spawns": {
            "count": spawn_count,
            "average_position": (spawn_avg_x, spawn_avg_y)
        },
        "towers": {
            "count": tower_count,
            "average_position": (tower_avg_x, tower_avg_y)
        }
    }