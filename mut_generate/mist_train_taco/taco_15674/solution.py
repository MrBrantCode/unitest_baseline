"""
QUESTION:
Consider a 2d plane and a Robot which is located at (0,0) who can move only one unit step at a time in any direction i.e. if its initial position is (x,y), he can go to positions (x + 1, y), (x - 1, y), (x, y + 1) or (x, y - 1). Now Given three integers a,b (denoting the final position where the robot has to reach), and x. Find out if the Robot can reach the final position in exactly x steps.
 
Example 1:
Input:
a = 5, b = 5, x = 11
Output:
0
Explanation:
No matter how the Robot moves,
the Robot won't be able to reach
point (5,5) in exactly 11 moves.
Example 2:
Input:
a = 10, b = 15, x = 25
Output:
1
Explanation:
The Robot can move 10 times towards
positive x-axis and then 15 times
towards positive y-axis to reach (10,15).
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function canReach() which takes 3 Integers a,b and x as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
-10^{9} <= a,b <= 10^{9}
1 <= x <= 2*10^{9}
"""

def can_reach(a: int, b: int, x: int) -> int:
    # Calculate the Manhattan distance from (0,0) to (a,b)
    distance = abs(a) + abs(b)
    
    # Check if the distance is exactly x
    if distance == x:
        return 1
    
    # Check if the distance is less than x and the difference is even
    if distance < x and (x - distance) % 2 == 0:
        return 1
    
    # Otherwise, it's not possible
    return 0