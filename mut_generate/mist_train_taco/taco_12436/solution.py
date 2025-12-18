"""
QUESTION:
Spring is interesting season of year. Chef is thinking about different things, but last time he thinks about interesting game - "Strange Matrix". 
Chef has a matrix that consists of n rows, each contains m elements. Initially, the element aij of matrix equals j. (1 ≤ i ≤ n, 1 ≤ j ≤ m). 
Then p times some element aij is increased by 1. 
Then Chef needs to calculate the following: 

- For each row he tries to move from the last element (with number m) to the first one (with the number 1). 
- While staying in aij Chef can only move to aij - 1 only if aij - 1 ≤ aij. 
- The cost of such a movement is aij - aij - 1.
- Otherwise Chef can't move and lose (in this row).
- If Chef can move from the last element of the row to the first one, then the answer is the total cost of all the movements. 
- If Chef can't move from the last element of the row to the first one, then the answer is -1. 

Help Chef to find answers for all the rows after P commands of increasing. 

-----Input-----

- The first line contains three integers n, m and p denoting the number of rows, the number of elements a single row and the number of increasing commands. 
- Each of next p lines contains two integers i and j denoting that the element aij  is increased by one. 

-----Output-----
- For each row in a single line print the answer after the P increasing commands.

-----Constraints-----
- 1 ≤ n, m, p ≤ 10 ^ 5
- 1 ≤ i ≤ n
- 1 ≤ j ≤ m

-----Example-----
Input:
4 4 6
2 2
3 2 
3 2 
4 3
4 4
4 3

Output:
3
3
-1
4


-----Explanation-----

Here is the whole matrix after P commands:
1 2 3 4
1 3 3 4
1 4 3 4
1 2 5 5

Explanations to the answer: 
- The first line is without changes: 4-3=1, 3-2=1, 2-1=1. answer = 3. 
- The second line: 4-3=1, 3-3=0, 3-1=2. The answer is 3. 
- The third line: 4-3=1, 3-4=-1, Chef can't move to the first number here. Therefore, the answer is -1. 
- The fourth line: 5-5=0, 5-2=3, 2-1=1. The answer is 4.
"""

def calculate_row_costs(n, m, p, commands):
    # Initialize the matrix with default values
    arr = [dict() for _ in range(n)]
    
    # Apply the commands to the matrix
    for (i, j) in commands:
        i -= 1  # Convert to 0-based index
        j -= 1  # Convert to 0-based index
        if j not in arr[i]:
            arr[i][j] = j + 1
        else:
            arr[i][j] += 1
    
    # Function to calculate the cost for a single row
    def chefbm(arr, i):
        for (e, f) in arr[i].items():
            if e == m - 1:
                continue
            if e + 1 in arr[i]:
                c = arr[i][e + 1]
            else:
                c = e + 1
            if arr[i][e] > c:
                return -1
        y = arr[i][m - 1] if m - 1 in arr[i] else m - 1
        x = arr[i][0] if 0 in arr[i] else 0
        return y - x
    
    # Calculate the result for each row
    results = []
    for i in range(n):
        results.append(chefbm(arr, i))
    
    return results