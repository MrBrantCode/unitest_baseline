"""
QUESTION:
There are N bikes and each can cover 100 km when fully fueled. What is the maximum amount of distance you can go using N bikes? You may assume that all bikes are similar and a bike takes 1 litre to cover 1 km.
Note: The answer may contain decimal value but print the integer value of the float value obtained.
 
Example 1:
Input:
N = 2
Output:
150
Explanation:
The 2 bikes can travel 50 Kms
together and then, the fuel of
the First bike can be transferred
to the Second, resulting in a full
tank for the second bike. The 2nd bike
will be able to travel 100 Kms more.
So, the Ouput is 150.
Example 2:
Input:
N = 3
Output:
183
Explanation:
The 3 bikes can travel 33.33 Kms
together and then, rest of the fuel of
the First bike can be transferred
to the Second and Third bike, resulting in
a full tank for the second and third bike.
The 2nd and 3rd bike can travel 50 Kms more
together. Now, both the bikes will have half
fuel. The 2nd bike can transfer the fuel to
the 3rd. The 3rd will have a full tank and
travel 100 Kms more. So, the Distance
will be 183.33
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxDist() which takes an Integer N as input and returns the answer.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
"""

def calculate_max_distance(N: int) -> int:
    dist_covered = 0
    fuel = 100
    while N > 0:
        dist_covered += fuel / N
        N -= 1
    return int(dist_covered)