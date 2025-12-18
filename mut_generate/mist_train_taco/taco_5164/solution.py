"""
QUESTION:
There are n cows playing poker at a table. For the current betting phase, each player's status is either "ALLIN", "IN", or "FOLDED", and does not change throughout the phase. To increase the suspense, a player whose current status is not "FOLDED" may show his/her hand to the table. However, so as not to affect any betting decisions, he/she may only do so if all other players have a status of either "ALLIN" or "FOLDED". The player's own status may be either "ALLIN" or "IN".

Find the number of cows that can currently show their hands without affecting any betting decisions.


-----Input-----

The first line contains a single integer, n (2 ≤ n ≤ 2·10^5). The second line contains n characters, each either "A", "I", or "F". The i-th character is "A" if the i-th player's status is "ALLIN", "I" if the i-th player's status is "IN", or "F" if the i-th player's status is "FOLDED".


-----Output-----

The first line should contain a single integer denoting the number of players that can currently show their hands.


-----Examples-----
Input
6
AFFAAA

Output
4

Input
3
AFI

Output
1



-----Note-----

In the first sample, cows 1, 4, 5, and 6 can show their hands. In the second sample, only cow 3 can show her hand.
"""

def count_showable_hands(n: int, statuses: str) -> int:
    # Count the occurrences of each status
    count_A = statuses.count('A')
    count_I = statuses.count('I')
    count_F = statuses.count('F')
    
    # Determine the number of cows that can show their hands
    if count_I == 0:
        return count_A
    elif count_I == 1:
        return 1
    else:
        return 0