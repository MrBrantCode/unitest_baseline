"""
QUESTION:
Create a function `simulate_battle` that simulates a turn-based battle between two characters, `John` and `Alex`. Each character has attributes for name, health, attack, defense, and speed, as well as a special attack attribute. The function should alternate between the characters' turns, checking if the current character can use their special attack and updating the other character's health accordingly. The function should continue until one character's health reaches 0 or below, then return the final health of both characters.

The `John` and `Alex` classes should inherit from a base `Character` class with the following attributes: `name`, `health`, `attack`, `defense`, and `speed`. The `John` class should have 100 health, 20 attack, 10 defense, and 5 speed, while the `Alex` class should have 120 health, 15 attack, 15 defense, and 7 speed. Both classes should have a special attack attribute with a value of 30 for `John` and 20 for `Alex`.
"""

class Character:
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

class John(Character):
    def __init__(self):
        super().__init__("John", 100, 20, 10, 5)
        self.special_attack = 30

class Alex(Character):
    def __init__(self):
        super().__init__("Alex", 120, 15, 15, 7)
        self.special_attack = 20

def simulate_battle(john: John, alex: Alex):
    current_character = john
    other_character = alex
    while john.health > 0 and alex.health > 0:
        # Check if the current character can use their special attack
        if current_character.health < 30:
            other_character.health -= current_character.special_attack
        else:
            other_character.health -= current_character.attack
        # Check if the other character is still alive
        if other_character.health <= 0:
            break
        # Swap the current and other characters
        current_character, other_character = other_character, current_character
    return john.health, alex.health