"""
QUESTION:
Given $N *M$ matrix containing elements either $1$ or $0$ and string S of length $N+M-1$ containing characters $0$ or $1$. Your task is to make all the  paths from top left corner to the  bottom right corner of the matrix same as the  given string .You can perform two types of operations any time .Path means you can only allow it to take right or down. 
Operations :
- Changing the matrix elements from $1$ to $0$ or vice versa  will cost P rupees per element.
- Changing the character of string  from $1$ to $0$ or vice versa  will cost Q rupees per character.
You have to  minimize the cost, (possibly 0) .

-----Input:-----
- First line of input contains the total no. of test cases $T$. 
- For every test case, first line of input contains two spaced positive integers, $N$ and $M$.
- Next $N$ lines contains $M$-spaced integers which can be only $0$ or $1$.
- Next line of input contains a string $S$ of length $N+M-1$.
- Last line of input contains two spaced integers, $P$ and $Q$.

-----Output:-----
- $You$ $have$ $to$ $print$ $the$ $minimum$ $cost .$

-----Constraints-----
- $1 \leq T \leq 20$
- $1 \leq N, M \leq 1000$
- $|S| = N+M-1$
- $0 \leq P, Q \leq 1000$The input/output is quite large, please use fast reading and writing methods.

-----Sample Input-----
2
3 3
1 0 1
0 1 1
1 1 0
10111
10 5
3 3 
0 0 1
0 1 1
0 1 1
00011
2 9

-----Sample Output-----
5
4

-----Explanation-----
- You can  change the last element of the matrix and also can change the last element of string but the minimum cost will produce by changing string element , therefore it will cost 5 rupees.
"""

def calculate_minimum_cost(matrix, path_string, cost_matrix_change, cost_string_change):
    n = len(matrix)
    m = len(matrix[0])
    ans = [[0, 0] for _ in range(n + m)]
    
    # Count the number of 0s and 1s in each diagonal
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                ans[i + j][0] += 1
            else:
                ans[i + j][1] += 1
    
    total_cost = 0
    
    # Calculate the minimum cost for each diagonal
    for i in range(n + m - 1):
        if path_string[i] == '0':
            cost_if_change_matrix = ans[i][1] * cost_matrix_change
            cost_if_change_string = cost_string_change + ans[i][0] * cost_matrix_change
            total_cost += min(cost_if_change_matrix, cost_if_change_string)
        else:
            cost_if_change_matrix = ans[i][0] * cost_matrix_change
            cost_if_change_string = cost_string_change + ans[i][1] * cost_matrix_change
            total_cost += min(cost_if_change_matrix, cost_if_change_string)
    
    return total_cost