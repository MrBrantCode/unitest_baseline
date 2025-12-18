"""
QUESTION:
Formula 1 officials decided to introduce new competition. Cars are replaced by space ships and number of points awarded can differ per race.

Given the current ranking in the competition and points distribution for the next race, your task is to calculate the best possible ranking for a given astronaut after the next race. It's guaranteed that given astronaut will have unique number of points before the race.


-----Input-----

The first line contains two integer numbers $N$ ($1 \leq N \leq 200000$) representing number of F1 astronauts, and current position of astronaut $D$ ($1 \leq D \leq N$) you want to calculate best ranking for (no other competitor will have the same number of points before the race).

The second line contains $N$ integer numbers $S_k$ ($0 \leq S_k \leq 10^8$, $k=1...N$), separated by a single space, representing current ranking of astronauts. Points are sorted in non-increasing order.

The third line contains $N$ integer numbers $P_k$ ($0 \leq P_k \leq 10^8$, $k=1...N$), separated by a single space, representing point awards for the next race. Points are sorted in non-increasing order, so winner of the race gets the maximum number of points.


-----Output-----

Output contains one integer number — the best possible ranking for astronaut after the race. If multiple astronauts have the same score after the race, they all share the best ranking.


-----Example-----
Input
4 3
50 30 20 10
15 10 7 3

Output
2



-----Note-----

If the third ranked astronaut wins the race, he will have 35 points. He cannot take the leading position, but he can overtake the second position if the second ranked astronaut finishes the race at the last position.
"""

def calculate_best_ranking(N, D, current_ranking, points_awards):
    # Calculate the maximum possible points for the given astronaut after the race
    x = current_ranking[D - 1] + points_awards[0]
    
    # Initialize the counter for potential lower rankings
    p = 0
    
    # If the given astronaut is currently in the first position, they will remain in the first position
    if D == 1:
        return 1
    
    # Iterate over the current ranking up to the position before the given astronaut
    for i in range(D - 1):
        # Check if the current astronaut can be overtaken by the given astronaut
        if current_ranking[i] + points_awards[-1] <= x:
            p += 1
            # Remove the last element from points_awards as it is used
            del points_awards[-1]
    
    # The best possible ranking is the current position minus the number of overtakes
    best_ranking = D - p
    return best_ranking