"""
QUESTION:
Hideo Kojima has just quit his job at Konami. Now he is going to find a new place to work. Despite being such a well-known person, he still needs a CV to apply for a job.

During all his career Hideo has produced n games. Some of them were successful, some were not. Hideo wants to remove several of them (possibly zero) from his CV to make a better impression on employers. As a result there should be no unsuccessful game which comes right after successful one in his CV.

More formally, you are given an array s_1, s_2, ..., s_{n} of zeros and ones. Zero corresponds to an unsuccessful game, one — to a successful one. Games are given in order they were produced, and Hideo can't swap these values. He should remove some elements from this array in such a way that no zero comes right after one.

Besides that, Hideo still wants to mention as much games in his CV as possible. Help this genius of a man determine the maximum number of games he can leave in his CV.


-----Input-----

The first line contains one integer number n (1 ≤ n ≤ 100).

The second line contains n space-separated integer numbers s_1, s_2, ..., s_{n} (0 ≤ s_{i} ≤ 1). 0 corresponds to an unsuccessful game, 1 — to a successful one.


-----Output-----

Print one integer — the maximum number of games Hideo can leave in his CV so that no unsuccessful game comes after a successful one.


-----Examples-----
Input
4
1 1 0 1

Output
3

Input
6
0 1 0 0 1 0

Output
4

Input
1
0

Output
1
"""

def max_games_in_cv(n, games):
    # Initialize a list to store the maximum number of games for each possible split point
    max_games = [0] * (n + 1)
    
    # Calculate the number of successful games after each split point
    successful_games_after = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        successful_games_after[i] = successful_games_after[i + 1] + (1 if games[i] == 1 else 0)
    
    # Calculate the number of unsuccessful games before each split point
    unsuccessful_games_before = [0] * (n + 1)
    for i in range(1, n + 1):
        unsuccessful_games_before[i] = unsuccessful_games_before[i - 1] + (1 if games[i - 1] == 0 else 0)
    
    # Calculate the maximum number of games for each split point
    for i in range(n + 1):
        max_games[i] = unsuccessful_games_before[i] + successful_games_after[i]
    
    # Return the maximum value from the max_games list
    return max(max_games)