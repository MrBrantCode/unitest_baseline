"""
QUESTION:
Implement the `get_closest_enemy` method to find the closest enemy sprite to a given position (x, y) within a specified maximum radius. The method should have the following signature:

`get_closest_enemy(x, y, max_radius, sprites, metric_func)`

- The method takes the position coordinates (x, y), a maximum radius, a list of sprites, and a metric function as input.
- The metric function is used to calculate the distance between two points.
- The method should return the closest enemy sprite within the maximum radius. If no enemy sprites are found within the radius, return None.
- It is assumed that the sprites list contains instances of the `pygame.sprite.Sprite` class and the metric_func is a function that takes two position tuples (x1, y1) and (x2, y2) as input and returns the distance between the two positions.
"""

def get_closest_enemy(x, y, max_radius, sprites, metric_func):
    closest_enemy = None
    closest_distance = float('inf')

    for sprite in sprites:
        sprite_pos = (sprite.rect.centerx, sprite.rect.centery)
        dist = metric_func((x, y), sprite_pos)
        if dist <= max_radius and dist < closest_distance:
            closest_enemy = sprite
            closest_distance = dist

    return closest_enemy