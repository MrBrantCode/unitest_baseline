"""
QUESTION:
Given a list S that initially contains a single value 0. Below are the Q queries of the following types:
	0 X: Insert X in the list
	1 X: For every element A in S, replace it by A XOR X.
Print all the element in the list in increasing order after performing the given Q queries.
 
Example 1:
Input:
N = 5
Q[] = {{0, 6}, {0, 3}, {0, 2}, {1, 4}, {1, 5}}
Output:
1 2 3 7
Explanation:
[0] (initial value)
[0 6] (add 6 to list)
[0 6 3] (add 3 to list)
[0 6 3 2] (add 2 to list)
[4 2 7 6] (XOR each element by 4)
[1 7 2 3] (XOR each element by 5)
Thus sorted order after performing
queries is [1 2 3 7] 
Example 2:
Input:
N = 3
Q[] = {{0, 2}, {1, 3}, {0, 5}} 
Output :
1 3 5
Explanation:
[0] (initial value)
[0 2] (add 2 to list)
[3 1] (XOR each element by 3)
[3 1 5] (add 5 to list)
Thus sorted order after performing
queries is [1 3 5].
Your Task:  
You don't need to read input or print anything. Your task is to complete the function constructList() which takes an integer N the number of queries and Q a list of lists of length 2 denoting the queries as input and returns the final constructed list.
Expected Time Complexity: O(N*log(N))
Expected Auxiliary Space: O(L), where L is only used for output specific requirements.
Constraints:
1 ≤ Length of Q ≤ 10^{5}
"""

def construct_final_list(N, Q):
    ans = []
    xor = 0
    for i in range(N - 1, -1, -1):
        if Q[i][0] == 0:
            ans.append(Q[i][1] ^ xor)
        else:
            xor ^= Q[i][1]
    ans.append(xor)
    ans.sort()
    return ans