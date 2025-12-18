"""
QUESTION:
Implement a function named `update_strategy` that takes a dictionary `loot_fight` and a string `current_strategy` as input, and returns an updated strategy. 

The `loot_fight` dictionary contains a key 'battle' with a sub-key 'result' indicating the outcome of the battle. If the battle is successful (result is True), the win streak is stored in `loot_fight['_u']['WinStreak@Value']`. 

The function should return the updated strategy based on the following conditions:
- If the battle result is successful and the win streak is greater than or equal to 10, the updated strategy should be 'aggressive'.
- If the battle result is successful and the win streak is less than 10, the updated strategy should be 'normal'.
- If the battle result is unsuccessful, the updated strategy should be 'defensive'.

The function signature should be `def update_strategy(loot_fight: dict, current_strategy: str) -> str`.
"""

def update_strategy(loot_fight: dict, current_strategy: str) -> str:
    if loot_fight['battle']['result']:
        win_streak = loot_fight['_u']['WinStreak@Value']
        if win_streak >= 10:
            return 'aggressive'
        else:
            return 'normal'
    else:
        return 'defensive'