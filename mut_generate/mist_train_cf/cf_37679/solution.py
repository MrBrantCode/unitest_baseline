"""
QUESTION:
Implement the game logic to control a player character and handle collision detection. Define a function to control the player character and detect collisions with enemy objects. The function should handle accelerating and decelerating the player character using up and down keys and detect if the player character collides with any enemy objects in the enemy_list. The player character's position should be updated based on its speed, and the game should restart when the player collides with an enemy object. The player character's initial position and speed are 0.
"""

class Player:
    def __init__(self):
        self.position = 0  
        self.speed = 0  

    def accelerate(self):
        self.speed += 1  

    def decelerate(self):
        self.speed -= 1  

    def move(self):
        self.position += self.speed  

    def check_collision(self, enemy_list):
        for enemy in enemy_list:
            if abs(self.position - enemy.position) < 2:
                return True  
        return False  

def control_player(player, enemy_list):
    player.move()
    return player.check_collision(enemy_list)