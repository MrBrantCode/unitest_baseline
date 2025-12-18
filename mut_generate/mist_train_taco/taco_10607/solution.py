"""
QUESTION:
Chef is playing in a T20 cricket match. In a match, Team A plays for 20 overs. In a single over, the team gets to play 6 times, and in each of these 6 tries, they can score a maximum of 6 runs. After Team A's 20 overs are finished, Team B similarly plays for 20 overs and tries to get a higher total score than the first team. The team with the higher total score at the end wins the match.

Chef is in Team B. Team A has already played their 20 overs, and have gotten a score of $R$. Chef's Team B has started playing, and have already scored $C$ runs in the first $O$ overs. In the remaining $20 - O$ overs, find whether it is possible for Chef's Team B to get a score high enough to win the game. That is, can their final score be strictly larger than $R$?

------ Input: ------
There is a single line of input, with three integers, $R, O, C$. 

------ Output: ------
Output in a single line, the answer, which should be "YES" if it's possible for Chef's Team B  to win the match and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

------ Constraints  ------
$0 ≤ C ≤ R ≤ 720$
$1 ≤ O ≤ 19$
$0 ≤ C ≤ 36 * O$

----- Sample Input 1 ------ 
719 18 648
----- Sample Output 1 ------ 
YES
----- explanation 1 ------ 
In the remaining $20-O = 2$ overs, Team B gets to play $2*6 = 12$ times, and in each try, they can get a maximum of 6 score. Which means that the maximum score that they can acheieve in these 2 overs is $12*6 = 72$. Thus, the maximum total score that Team B can achieve is $C+72 = 720$. $720$ is strictly more than Team A's score of $719$, and hence Chef's Team B can win this match.

----- Sample Input 2 ------ 
720 18 648
----- Sample Output 2 ------ 
NO
----- explanation 2 ------ 
Similar to the previous explanation, the maximum total score that Team B can achieve is $720$, which isn't strictly greater than Team A's $720$.Hence Chef's Team B can't win this match.
"""

def can_team_b_win(R: int, O: int, C: int) -> str:
    """
    Determines if Team B can win the match given the current scores and overs played.

    Parameters:
    - R (int): The total score of Team A.
    - O (int): The number of overs already played by Team B.
    - C (int): The current score of Team B.

    Returns:
    - str: "YES" if Team B can win, "NO" otherwise.
    """
    # Calculate the maximum possible score Team B can achieve in the remaining overs
    max_possible_score = (20 - O) * 36 + C
    
    # Determine if Team B can win
    if max_possible_score > R:
        return "YES"
    else:
        return "NO"