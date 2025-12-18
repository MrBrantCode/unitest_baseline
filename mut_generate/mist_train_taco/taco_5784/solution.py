"""
QUESTION:
# Back-Story

Every day I travel on the freeway.

When I am more bored than usual I sometimes like to play the following counting game I made up:

* As I join the freeway my count is ```0```
* Add ```1``` for every car that I overtake
* Subtract ```1``` for every car that overtakes me
* Stop counting when I reach my exit

What an easy game! What fun!

# Kata Task

You will be given
* The distance to my exit (km)
* How fast I am going (kph)
* Information about a lot of other cars 
 * Their time (relative to me) as I join the freeway. For example,
   * ```-1.5``` means they already passed my starting point ```1.5``` minutes ago
   * ```2.2``` means they will pass my starting point ```2.2``` minutes from now
 * How fast they are going (kph)

Find what is my "score" as I exit the freeway!

# Notes

* Assume all cars travel at a constant speeds

 Safety Warning 

If you plan to play this "game" remember that it is not really a game. You are in a **real** car.

There may be a temptation to try to beat your previous best score.

Please don't do that...
"""

def calculate_freeway_score(exit_distance, my_speed, cars):
    # Calculate the time it takes for me to reach the exit
    time_to_exit = exit_distance / my_speed
    
    # Initialize the score
    score = 0
    
    # Iterate over each car's information
    for (time_relative_to_me, car_speed) in cars:
        # Calculate the distance the car will travel relative to my exit point
        distance_relative_to_exit = exit_distance - (time_to_exit - time_relative_to_me / 60) * car_speed
        
        # Update the score based on whether the car is ahead or behind
        if time_relative_to_me <= 0:
            score += distance_relative_to_exit > 0
        else:
            score -= distance_relative_to_exit < 0
    
    return score