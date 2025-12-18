"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 
Spring is interesting season of year. Chef is thinking about different things, but last time he thinks about interesting game - "Strange Matrix". 
Chef has a matrix that consists of n rows, each contains m elements. Initially, the element a_{i}_{j} of matrix equals j. (1 ≤ i ≤ n, 1 ≤ j ≤ m). 
Then p times some element a_{i}_{j} is increased by 1. 
Then Chef needs to calculate the following: 
For each row he tries to move from the last element (with number m) to the first one (with the number 1). 
While staying in a_{i}_{j} Chef can only move to a_{i}_{j - 1} only if a_{i}_{j - 1} ≤ a_{i}_{j}. 
The cost of such a movement is a_{i}_{j} - a_{i}_{j - 1}.
Otherwise Chef can't move and lose (in this row).
If Chef can move from the last element of the row to the first one, then the answer is the total cost of all the movements. 
If Chef can't move from the last element of the row to the first one, then the answer is -1. 
Help Chef to find answers for all the rows after P commands of increasing. 

------ Input ------ 

The first line contains three integers n, m and p denoting the number of rows, the number of elements a single row and the number of increasing commands. 
Each of next p lines contains two integers i and j denoting that the element a_{i}_{j } is increased by one. 

------ Output ------ 

For each row in a single line print the answer after the P increasing commands.
 
------ Constraints ------ 

$1 ≤ n, m, p ≤ 10 ^ 5$
$1 ≤ i ≤ n$
$1 ≤ j ≤ m$

----- Sample Input 1 ------ 
4 4 6
2 2
3 2 
3 2 
4 3
4 4
4 3
----- Sample Output 1 ------ 
3
3
-1
4
----- explanation 1 ------ 

Here is the whole matrix after P commands:
1 2 3 4
1 3 3 4
1 4 3 4
1 2 5 5
Explanations to the answer: 
The first line is without changes: 4-3=1, 3-2=1, 2-1=1. answer = 3. 
The second line: 4-3=1, 3-3=0, 3-1=2. The answer is 3. 
The third line: 4-3=1, 3-4=-1, Chef can't move to the first number here. Therefore, the answer is -1. 
The fourth line: 5-5=0, 5-2=3, 2-1=1. The answer is 4.
"""

def calculate_row_costs(n, m, p, commands):
    scores = [m - 1 for _ in range(n)]
    coord = {}
    
    if m == 1:
        return scores
    
    for (i, j) in commands:
        if j == m:
            scores[i - 1] += 1
        elif j == 1:
            scores[i - 1] -= 1
        
        pair = (i, j)
        if pair not in coord:
            coord[pair] = 1
        else:
            coord[pair] += 1
    
    for (i, j) in coord:
        if j != m:
            condition = coord.get((i, j)) - coord.get((i, j + 1), 0) > 1
            if condition:
                scores[i - 1] = -1
    
    return scores