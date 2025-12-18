"""
QUESTION:
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, $\mbox{S}$.

Both players have to make substrings using the letters of the string $\mbox{S}$.

Stuart has to make words starting with consonants.

Kevin has to make words starting with vowels. 

The game ends when both players have made all possible substrings.

Scoring

A player gets +1 point for each occurrence of the substring in the string $\mbox{S}$.

For Example:

String $\mbox{S}$ = BANANA

Kevin's vowel beginning word = ANA

Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below: 

Your task is to determine the winner of the game and their score.

Function Description   

Complete the minion_game in the editor below.    

minion_game has the following parameters:   

string string: the string to analyze   

Prints   

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner   

Input Format

A single line of input containing the string $\mbox{S}$. 

Note: The string $\mbox{S}$ will contain only uppercase letters: $\left[{\mbox{A}-\mbox{Z}}\right]$.  

Constraints

$0<len(S)\leq10^6$

Sample Input
BANANA

Sample Output
Stuart 12

Note : 

Vowels are only defined as $\textit{AEIOU}$. In this problem, $\mathbf{Y}$ is not considered a vowel.
"""

def minion_game(string: str) -> tuple:
    vowels = set(['A', 'E', 'I', 'O', 'U'])
    vscore = 0
    cscore = 0
    
    for i in range(len(string)):
        score = len(string) - i
        if string[i] in vowels:
            vscore += score
        else:
            cscore += score
    
    if cscore > vscore:
        return ('Stuart', cscore)
    elif vscore > cscore:
        return ('Kevin', vscore)
    else:
        return ('Draw', 0)