"""
QUESTION:
There is a house with 4 levels.
In that house there is an elevator.
You can program this elevator to go up or down,
depending on what button the user touches inside the elevator.

Valid levels must be only these numbers: `0,1,2,3`

Valid buttons must be only these strings: `'0','1','2','3'` 

Possible return values are these numbers: `-3,-2,-1,0,1,2,3`

If the elevator is on the ground floor(0th level) 
and the user touches button '2'
the elevator must go 2 levels up,
so our function must return 2.

If the elevator is on the 3rd level
and the user touches button '0'
the elevator must go 3 levels down, so our function must return -3.

If the elevator is on the 2nd level,
and the user touches button '2'
the elevator must remain on the same level,
so we return 0.

We cannot endanger the lives of our passengers, 
so if we get erronous inputs, 
our elevator must remain on the same level.
So for example:

- `goto(2,'4')` must return 0, because there is no button '4' in the elevator.
- `goto(4,'0')` must return 0, because there is no level 4.
- `goto(3,undefined)` must return 0.
- `goto(undefined,'2')` must return 0.
- `goto([],'2')` must return 0 because the type of the input level is array instead of a number.
- `goto(3,{})` must return 0 because the type of the input button is object instead of a string.
"""

def elevator_move(current_level, button_pressed):
    valid_levels = [0, 1, 2, 3]
    valid_buttons = ['0', '1', '2', '3']
    
    if not isinstance(current_level, int) or not isinstance(button_pressed, str):
        return 0
    
    if current_level not in valid_levels or button_pressed not in valid_buttons:
        return 0
    
    target_level = int(button_pressed)
    return target_level - current_level