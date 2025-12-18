"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

Chef has obtained the results of a past Cook-Off. He wants to estimate the skill level of each contestant. The contestants can be classified with high probability (w.h.p.) based on the number of solved problems:

A contestant that solved exactly 0 problems is a beginner.
A contestant that solved exactly 1 problem is a junior developer.
A contestant that solved exactly 2 problems is a middle developer.
A contestant that solved exactly 3 problems is a senior developer.
A contestant that solved exactly 4 problems is a hacker.
A contestant that solved all five problems is Jeff Dean.

Please help Chef to identify the programming level of each participant. 

------ Input ------ 

The first line of the input contains a single integer N denoting the number of competitors.
N lines follow. The i-th of these lines contains five space-separated integers A_{i, 1}, A_{i, 2}, A_{i, 3}, A_{i, 4}, A_{i, 5}. The j-th of these integers (1 ≤ j ≤ 5) is 1 if the i-th contestant solved the j-th problem and 0 otherwise.

------ Output ------ 

For each participant, print a single line containing one string denoting Chef's classification of that contestant — one of the strings "Beginner", "Junior Developer", "Middle Developer", "Senior Developer", "Hacker", "Jeff Dean" (without quotes).

------ Constraints ------ 

$1 ≤ N ≤ 5000$
$0 ≤ A_{i, j} ≤ 1 for each valid i, j$

----- Sample Input 1 ------ 
7
0 0 0 0 0
0 1 0 1 0
0 0 1 0 0
1 1 1 1 1
0 1 1 1 0
0 1 1 1 1
1 1 1 1 0
----- Sample Output 1 ------ 
Beginner
Middle Developer
Junior Developer
Jeff Dean
Senior Developer
Hacker
Hacker
----- explanation 1 ------ 
The first contestant has no solved problems, therefore he is a beginner. The second contestant solved 2 problems (the second and fourth problem), therefore he has the skills of a middle developer. The third contestant solved 1 problem, therefore he's at the expected level of a junior developer. The fourth contestant solved 5 problems — we can guess it was Jeff Dean. The fifth contestant solved 3 problems, so he is a senior developer. And the last two contestants should be hackers because they solved exactly 4 problems each.
"""

def classify_contestant(problems_solved):
    # Ensure the input list has exactly 5 elements
    if len(problems_solved) != 5:
        raise ValueError("The list must contain exactly 5 elements.")
    
    # Calculate the number of problems solved
    num_solved = sum(problems_solved)
    
    # Determine the classification based on the number of problems solved
    if num_solved == 0:
        return 'Beginner'
    elif num_solved == 1:
        return 'Junior Developer'
    elif num_solved == 2:
        return 'Middle Developer'
    elif num_solved == 3:
        return 'Senior Developer'
    elif num_solved == 4:
        return 'Hacker'
    elif num_solved == 5:
        return 'Jeff Dean'
    else:
        raise ValueError("Invalid input: Each element in the list must be either 0 or 1.")