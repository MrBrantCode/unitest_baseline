"""
QUESTION:
This time, Karan has decided to leave his laptop aside and take part in a long jump event - Noodle Jump. This is a special type of long jump event - it consists of a number of long jumps, of varying lengths.

Assuming the positive x-axis as the track, the coordinates where he can put his foot are given. He cannot put his foot on or in-between any other coordinates.

Given the geek that he is, he has already calculated the maximum jump he can make. As usual, he is short of time. He asks you the coordinate from where he will not be able to proceed further. Since this is a special type of long jump event, his jumps are measured only when he steps on the very first allowed coordinate.
Input:

The first line of the input contains two space separated integers N and K. N denotes the total number of coordinates where he can step and K denotes his maximum jumping capacity.

Next line contains N space separated integers - the coordinates where he can step.

Output:

The coordinate where his race ends.

Constraints:

1 ≤ N ≤ 10^6

1 ≤ K ≤ 10^6

0 ≤ coordinate ≤ 10^9

SAMPLE INPUT
4 1
1 2 3 5

SAMPLE OUTPUT
3
"""

def find_last_jump_coordinate(coordinates, max_jump_capacity):
    # Sort the coordinates to ensure they are in ascending order
    coordinates.sort()
    
    # Iterate through the sorted coordinates to find the last jumpable coordinate
    for i in range(1, len(coordinates)):
        if coordinates[i] - coordinates[i-1] > max_jump_capacity:
            return coordinates[i-1]
    
    # If no such coordinate is found, return the last coordinate in the list
    return coordinates[-1]