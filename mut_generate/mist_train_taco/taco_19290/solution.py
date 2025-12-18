"""
QUESTION:
A smelt fishing tournament was held at Lake Hibara. The winner is the one who wins the most smelt.

Create a program that reads the list of participant numbers and the number of fish caught and outputs the number of winners and the number of fish caught. If there are multiple winners, output the one with the lowest participant number.



input

The input is given in the following format.


n
a1 v1
a2 v2
::
an vn


n (1 ≤ n ≤ 20) represents the number of participants and ai represents the participant number. Participant numbers are different integers between 1 and n. vi (0 ≤ vi ≤ 100) is the number of animals acquired by the participant ai.

output

Output the winner's participant number and the number of fish caught on one line separated by blanks.

Example

Input

6
1 14
2 25
3 42
4 11
5 40
6 37


Output

3 42
"""

def find_smelt_fishing_winner(participants):
    # Dictionary to store the number of fish caught as keys and list of participant numbers as values
    fish_dict = {}
    
    for participant, fish_count in participants:
        if fish_count not in fish_dict:
            fish_dict[fish_count] = []
        fish_dict[fish_count].append(participant)
    
    # Find the maximum number of fish caught
    max_fish_count = max(fish_dict)
    
    # Find the winner with the lowest participant number among those who caught the maximum fish
    winner = min(fish_dict[max_fish_count])
    
    return winner, max_fish_count