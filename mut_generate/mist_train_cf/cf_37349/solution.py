"""
QUESTION:
Implement the `NotKillingItselfAI` class with the following methods: `__init__(self, player, obstacles, max_speed, max_worse_distance, depth)`, `get_information(self)`, and `make_decision(self)`. The `__init__` method should initialize the AI with the current player's state, a list of obstacles, the maximum speed the player can move at, the maximum worse distance the player can tolerate, and the depth of the AI's search tree. The `get_information` method should return a string containing the AI's information, including the maximum speed, maximum worse distance, and depth, in the format "max_speed=x, max_worse_distance=y, depth=z". The `make_decision` method should analyze the game state and return a list of actions for the AI to take, with possible actions including `speed_up`, `change_nothing`, and `turn_right` from the `Action` enum. The class should not include any game state or player implementation details, and the `make_decision` method should be implemented with a basic decision-making logic that returns a list of actions based on the player's current speed.
"""

from enum import Enum

class Action(Enum):
    speed_up = 0
    change_nothing = 1
    turn_right = 2

def not_killing_itself_ai(player, obstacles, max_speed, max_worse_distance, depth):
    return NotKillingItselfAI(player, obstacles, max_speed, max_worse_distance, depth)

class NotKillingItselfAI:
    def __init__(self, player, obstacles, max_speed, max_worse_distance, depth):
        self.player = player
        self.obstacles = obstacles
        self.max_speed = max_speed
        self.max_worse_distance = max_worse_distance
        self.depth = depth

    def get_information(self):
        return f"max_speed={self.max_speed}, max_worse_distance={self.max_worse_distance}, depth={self.depth}"

    def make_decision(self):
        actions = []
        if self.player.speed < self.max_speed:
            actions.append(Action.speed_up)
        else:
            actions.append(Action.change_nothing)
        actions.append(Action.turn_right)
        return actions