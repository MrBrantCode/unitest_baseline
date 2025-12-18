"""
QUESTION:
Task

Create a top-down movement system that would feel highly responsive to the player. In your Update method you have to check for the keys that are currently being pressed, the keys correspond to the enum Direction shown below, based on which key is pressed or released your method should behave this way:

1) When a key is first pressed, the player has to change his direction to that of the current key, without moving

2) If the key is still being pressed during the next Update, the player will move towards his current direction using these vectors: (Up = { 0, +1 } , Down = { 0, -1 }, Left = { -1, 0 }, Right = { +1, 0 })

3) If a new key is pressed, it will gain precedence over the previous key and the player will act as per 1)

4-A) If the current key (A) is released, then the precedence will go back to the previous key (B) (or the one before it, if (B) is not pressed anymore, and so on), then the player will behave as per 1).

4-B) If the current key is released, and no other keys are being pressed, the player will stand still

5) If all keys are released at once, the player will not move nor change direction

6) If multiple keys are pressed at once, the order of precedence will be the following { Up, Down, Left, Right } 

Examples

    (n = pressed key, [n] = current key, p() = press, r() = release, (8,2,4,6 = up, down, left, right)):

    [] , p(8) -> [8] , p(4,6) -> 86[4] , r(6) -> 8[4] , r(4) -> [8] , r(8) -> []

    [] , p(2486) -> 642[8] , r(2,8) -> 6[4] , r(4,6) -> []

This is what you'll need to use in your code (NB: the tile coordinates cannot be changed, you'll need to assign a new Tile each time the player moves):

```python
class Tile:

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
            
    def __str__(self):
        return "({},{})".format(self._x, self._y)

class Input:

    @staticmethod
    def get_state(direction): # 2, 4, 6, 8
        return Input.STATES[direction] # pressed = true, released = false
```
"""

def update_player_movement(current_position, current_direction, pressed_states, previous_pressed, direction_stack):
    PREC = [8, 2, 4, 6]
    I_KEYS = {8: 0, 2: 1, 4: 2, 6: 3}
    MOVES = {8: (0, 1), 2: (0, -1), 4: (-1, 0), 6: (1, 0)}
    
    new_pressed = [d for (i, d) in enumerate(PREC) if not previous_pressed[i] and pressed_states[i]]
    not_released = next((d for d in direction_stack[::-1] if previous_pressed[I_KEYS[d]] and pressed_states[I_KEYS[d]]), None)
    released_lst = [d for (i, d) in enumerate(PREC) if previous_pressed[i] and (not pressed_states[i])]
    
    if new_pressed:
        new_direction = new_pressed[0]
        for t in new_pressed[::-1]:
            direction_stack.append(t)
    elif current_direction in released_lst:
        new_direction = not_released or current_direction
    elif not_released:
        current_position = (current_position[0] + MOVES[not_released][0], current_position[1] + MOVES[not_released][1])
        new_direction = current_direction
    else:
        new_direction = current_direction
    
    for t in released_lst:
        if t in direction_stack:
            direction_stack.remove(t)
    
    return current_position, new_direction, pressed_states, direction_stack