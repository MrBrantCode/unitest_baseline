"""
QUESTION:
Sona is in-charge of inviting the guest. She don't know how much far they are from her place. She knows the guest house co-ordinates (gx,gy)and the co-ordinates of the place where she is standing(sx,sy). Help her to calculate the distance between the guest house and her place. 

Input

First line contains guest house co-odinates gx,gy and the second line contains Sona's coordinates sx,sy

Output

Print the distance and round off it to 5 digits

constraints

1< = gx,gy,sx,sy< = 10

SAMPLE INPUT
2 5
2 6

SAMPLE OUTPUT
1.00000

Explanation

Sona is in-charge of inviting the guest. She don't know how much far they are from her place. She knows the guest house co-ordinates and the co-ordinates of the place where she is standing. Help her to calculate the distance between the guest house and her place.
"""

def calculate_distance(gx, gy, sx, sy):
    """
    Calculate the distance between the guest house and Sona's position.

    Parameters:
    gx (int): The x-coordinate of the guest house.
    gy (int): The y-coordinate of the guest house.
    sx (int): The x-coordinate of Sona's position.
    sy (int): The y-coordinate of Sona's position.

    Returns:
    float: The distance between the guest house and Sona's position, rounded to 5 decimal places.
    """
    p = pow((gx - sx), 2) + pow((gy - sy), 2)
    dist = pow(p, 0.5)
    return round(dist, 5)