"""
QUESTION:
Consider you have an infinitely long binary tree having the pattern as below
               1
            /     \
           2      3  
         /  \     /   \
        4  5    6  7
    .  .  .  .   .  .  .  . 
Given two nodes with values x and y, the task is to find the length of the shortest path between the two nodes.
Example 1:
Input:
X = 1
Y = 3
Output:
1
Explanation:
3 is the child of 1 so, 
distance between them is 1.
Example 2:
Input:
X = 2
Y = 2
Output:
0
Explanation:
There is no node between 2 and 2.
Your Task: 
You don't need to read input or print anything. Your task is to complete the function distance() which take integers X and Y as input parameters and returns the distance between X and Y in the infinitely long tree.
 
Expected Time Complexity: O(log (y - x))
Expected Auxiliary Space: O(1)
Constraints:
1<=X,Y<=10^{7}
"""

def find_shortest_path_length(X: int, Y: int) -> int:
    if X == Y:
        return 0
    
    distance = 0
    while X != Y:
        if X > Y:
            X = X // 2
        else:
            Y = Y // 2
        distance += 1
    
    return distance