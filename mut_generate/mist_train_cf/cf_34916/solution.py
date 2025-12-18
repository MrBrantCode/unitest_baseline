"""
QUESTION:
Write a function `get_modified_stats(race, stats)` that takes a string `race` and a list of integers `stats` as input, where `stats` represents the base stats in the order: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma. The function should return a dictionary containing the modified stats for the given `race`. The function should support at least "human" and "half-orc" races, where "human" has no stat modifiers and "half-orc" has +2 Strength and -2 Intelligence modifiers. If the input `race` is not supported, the function should return an error message.
"""

def get_modified_stats(race, stats):
    modified_stats = dict(zip(["Str", "Dex", "Con", "Int", "Wis", "Cha"], stats))
    if race == "human":
        return modified_stats
    elif race == "half-orc":
        modified_stats["Str"] += 2
        modified_stats["Int"] -= 2
        return modified_stats
    else:
        return "Race not found"