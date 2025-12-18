"""
QUESTION:
A study has shown that playing a musical instrument helps in increasing one's IQ by 7 points.
Chef knows he can't beat Einstein in physics, but he wants to try to beat him in an IQ competition.

You know that Einstein had an IQ of 170, and Chef currently has an IQ of X.

Determine if, after learning to play a musical instrument, Chef's IQ will become strictly greater than Einstein's.

Print "Yes" if it is possible for Chef to beat Einstein, else print "No" (without quotes).

You may print each character of the string in either uppercase or lowercase (for example, the strings yEs, yes, Yes, and YES will all be treated as identical).

------ Input Format ------ 

- The first and only line of input will contain a single integer X, the current IQ of Chef.

------ Output Format ------ 

- For each testcase, output in a single line "Yes" or "No"
- You may print each character of the string in either uppercase or lowercase (for example, the strings yEs, yes, Yes, and YES will all be treated as identical).

------ Constraints ------ 

$100 ≤ X ≤ 169$

------ subtasks ------ 

Subtask #1 (100 points): Original constraints

----- Sample Input 1 ------ 
165
----- Sample Output 1 ------ 
Yes
----- explanation 1 ------ 
After learning a musical instrument, Chef's final IQ will be $165+7=172$. Since $172 > 170$, Chef can beat Einstein.

----- Sample Input 2 ------ 
120
----- Sample Output 2 ------ 
No
----- explanation 2 ------ 
After learning a musical instrument, Chef's final IQ will be $120+7=127$. Since $127 < 170$, Chef cannot beat Einstein.
"""

def can_chef_beat_einstein(chef_iq: int) -> str:
    """
    Determines if Chef's IQ after learning to play a musical instrument will be greater than Einstein's IQ.

    Parameters:
    chef_iq (int): The current IQ of Chef.

    Returns:
    str: "Yes" if Chef's IQ after learning to play a musical instrument is greater than 170, otherwise "No".
    """
    einstein_iq = 170
    increased_iq = chef_iq + 7
    if increased_iq > einstein_iq:
        return "Yes"
    else:
        return "No"