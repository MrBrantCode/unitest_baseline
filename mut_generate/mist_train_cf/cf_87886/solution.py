"""
QUESTION:
Create a class constructor for a Unicorn class with parameters name, color, and age. The constructor should initialize a dictionary of magical abilities for each unicorn object, where each magical ability is a key with a boolean value indicating whether the unicorn possesses that ability or not. The magical abilities should include nested dictionaries for specific categories of abilities, where each category is a key with a dictionary of specific abilities as its value. The constructor should not take any magical abilities as arguments, and all abilities should be initially set to False.
"""

def entrance(name, color, age):
    magical_abilities = {
        "healing": {
            "regeneration": False,
            "healing touch": False,
            "aura healing": False
        },
        "teleportation": {
            "instant teleportation": False,
            "dimensional travel": False,
            "teleportation circle": False
        },
        "elemental manipulation": {
            "fire manipulation": False,
            "water manipulation": False,
            "earth manipulation": False,
            "air manipulation": False
        }
    }
    return {
        "name": name,
        "color": color,
        "age": age,
        "magical_abilities": magical_abilities
    }