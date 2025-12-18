"""
QUESTION:
It’s time to find out which player is consistent in cricket. You need to calculate the average of a player based on his score. Player average is defined as total runs scored by a player in N matches divided by the number of matches in which he gets out.
 
Example 1:
Input: run = {10, 101, 49}, 
status = {"out", "notout", "out"}
Output: 80
Explanation: Total run = 10 + 101 + 49 = 160.
2 times the player gets out.
So, Average = 160 / 2 = 80.
Example 2:
Input: run = {6, 67, 5}, status = {"notout", 
"notout", "notout"}.
Output: -1
Explanation: Not possible to determine average.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function Average() which takes a list of runs and a list of status of the player in every match and retruns ceil value of the average. If not possible returns -1.
 
Expected Time Complexity: O(n) where n is the number of matches 
Expected Space Complexity: O(1)
 
Constraints:
1 <= No. of matches <= 500
1 <= run scored in every match <= 300
"""

import math

def calculate_player_average(runs, status):
    total_runs = sum(runs)
    if 'out' not in status:
        return -1
    else:
        count_out = status.count('out')
        return math.ceil(total_runs / count_out)