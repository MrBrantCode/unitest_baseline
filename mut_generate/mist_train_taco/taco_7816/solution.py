"""
QUESTION:
B: Yamanote-line Game-Yamanote-line Game-

Bean (?) Knowledge

The Yamanote line is convenient. The reason is that you can ride as many laps as time allows just by paying 130 yen. However, if you board with a ticket, you must be careful about the valid time of the ticket. It seems safe with an IC card. Taking advantage of the characteristics of the Yamanote Line, there are people in the suburbs of Tokyo who are swayed by trains and devour their sleep. By the way, the questioner of this question has never done it. It's rare for a station employee to find out, but I don't recommend it because it would be annoying.

Problem statement

Let's play a game that utilizes the characteristics of the Yamanote Line. Here, for generalization, there are N stations numbered from 1 to N, and the stations are lined up in the order of 1, 2, ..., N, and you can go to any station from each station. Let's consider the Yamanote Line Modoki as a route that can be boarded for d yen. The game follows the rules below.

* Select your favorite station as the starting point and board the Yamanote Line Modoki for d yen.
* After that, get off at any station and get on again.
* The game ends when you get off at the station where you started.
* If you get off at the i-th station, you can get a reward of p_i yen.
* However, you cannot get the reward again at the station where you got the reward once.
* Also, it costs d yen to get on the Yamanote Line Modoki again after getting off.



Now, how many yen can you make up to? Please give it a try.

Input format


N d
p_1 p_2… p_N


All inputs consist of integers. On the first line, the number N of Modoki stations on the Yamanote line and the fare d are given separated by blanks. On the second line, the rewards received at each station are given separated by blanks, and the i-th value p_i represents the reward for station i.

Constraint

* 3 ≤ N ≤ 1 {,} 000
* 1 ≤ d ≤ 1 {,} 000
* 1 ≤ p_i ≤ 1 {,} 000 (1 ≤ i ≤ N)



Output format

Output the maximum amount of money you can get in the game on one line. If you can't get more than 1 yen, print "kusoge" on one line. The end of the output should be newline and should not contain extra characters.

Input example 1


5 130
130 170 100 120 140


Output example 1


50

Input example 2


3 100
100 90 65


Output example 2


kusoge

Input example 3


6 210
300 270 400 330 250 370


Output example 3


660

Input example 4


4 540
100 460 320 280


Output example 4


kusoge





Example

Input

5 130
130 170 100 120 140


Output

50
"""

def calculate_max_reward(N, d, rewards):
    # Calculate the profit for each station by subtracting the fare
    profits = [reward - d for reward in rewards if reward - d >= 0]
    
    # Sum the profits to get the total maximum reward
    max_reward = sum(profits)
    
    # If the total reward is 0 or less, return "kusoge"
    if max_reward <= 0:
        return "kusoge"
    
    # Otherwise, return the total maximum reward
    return max_reward