"""
QUESTION:
A carpet shop sells carpets in different varieties. Each carpet can come in a different roll width and can have a different price per square meter. 

Write a function `cost_of_carpet` which calculates the cost (rounded to 2 decimal places) of carpeting a room, following these constraints:

* The carpeting has to be done in one unique piece. If not possible, retrun `"error"`.
* The shop sells any length of a roll of carpets, but always with a full width.
* The cost has to be minimal.
* The length of the room passed as argument can sometimes be shorter than its width (because we define these relatively to the position of the door in the room).
* A length or width equal to zero is considered invalid, return `"error"` if it occurs.


INPUTS:

`room_width`, `room_length`, `roll_width`, `roll_cost` as floats.

OUTPUT:

`"error"` or the minimal cost of the room carpeting, rounded to two decimal places.
"""

def calculate_carpet_cost(room_width, room_length, roll_width, roll_cost):
    # Ensure room_width and room_length are sorted such that room_width <= room_length
    (room_width, room_length) = sorted((room_width, room_length))
    
    # Check for invalid dimensions
    if room_width == 0 or room_length == 0:
        return "error"
    
    # Check if the roll width is sufficient to cover the room width
    if roll_width < room_width:
        return "error"
    
    # Calculate the cost based on the minimal required length of carpet
    if roll_width >= room_length:
        # If the roll width is greater than or equal to the room length, we can use the room length
        cost = room_length * roll_width * roll_cost
    else:
        # Otherwise, we need to use the room width (since it's the smaller dimension)
        cost = room_width * roll_width * roll_cost
    
    # Return the cost rounded to two decimal places
    return round(cost, 2)