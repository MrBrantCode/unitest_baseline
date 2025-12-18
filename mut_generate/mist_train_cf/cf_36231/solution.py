"""
QUESTION:
Implement a function `nextMove(gamedata)` that determines the next move for a snake in a grid-based game. The function takes a dictionary `gamedata` as input, which contains information about the game state, including the position of the snake, the positions of the food, and the dimensions of the grid.

The next move should be one of the strings: "up", "down", "left", or "right". The snake should move towards the nearest food item. If there are multiple food items at the same distance, the snake should prioritize the one that leads it closer to the edge of the grid. If there are no food items, the snake should continue moving in its current direction.
"""

def nextMove(gamedata):
    head = gamedata['you']['body'][0]
    food_positions = gamedata['food']
    grid_width = gamedata['board']['width']
    grid_height = gamedata['board']['height']

    def distance(p1, p2):
        return abs(p1['x'] - p2['x']) + abs(p1['y'] - p2['y'])

    def is_valid_move(x, y):
        return 0 <= x < grid_width and 0 <= y < grid_height

    def find_nearest_food():
        min_distance = float('inf')
        nearest_food = None
        for food in food_positions:
            dist = distance(head, food)
            if dist < min_distance:
                min_distance = dist
                nearest_food = food
            elif dist == min_distance:
                if (nearest_food['x'] == 0 or nearest_food['x'] == grid_width - 1) and food['x'] != 0 and food['x'] != grid_width - 1:
                    nearest_food = food
                elif (nearest_food['y'] == 0 or nearest_food['y'] == grid_height - 1) and food['y'] != 0 and food['y'] != grid_height - 1:
                    nearest_food = food
        return nearest_food

    nearest_food = find_nearest_food()
    if nearest_food:
        if nearest_food['x'] < head['x']:
            return "left"
        elif nearest_food['x'] > head['x']:
            return "right"
        elif nearest_food['y'] < head['y']:
            return "up"
        elif nearest_food['y'] > head['y']:
            return "down"
    else:
        # continue moving in the current direction
        # implement logic to avoid obstacles if needed
        pass