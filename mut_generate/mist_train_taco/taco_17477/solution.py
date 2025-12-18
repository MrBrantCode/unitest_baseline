"""
QUESTION:
Chingel is practicing for a rowing competition to be held on this saturday. He is trying his best to win this tournament for which he needs to figure out how much time it takes to cover a certain distance. 

**Input**

You will be provided with the total distance of the journey, speed of the boat and whether he is going downstream or upstream. The speed of the stream and direction of rowing will be given as a string. Check example test cases!

**Output**

The output returned should be the time taken to cover the distance. If the result has decimal places, round them to 2 fixed positions.

`Show some love ;) Rank and Upvote!`
"""

def calculate_rowing_time(distance, boat_speed, stream):
    direction, stream_speed = stream.split()
    stream_speed = int(stream_speed)
    
    if direction == 'D':
        effective_speed = boat_speed + stream_speed
    elif direction == 'U':
        effective_speed = boat_speed - stream_speed
    else:
        raise ValueError("Invalid stream direction. Use 'D' for downstream or 'U' for upstream.")
    
    return round(distance / effective_speed, 2)