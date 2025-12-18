"""
QUESTION:
For her next karate demonstration, Ada will break some bricks.
Ada stacked three bricks on top of each other. Initially, their widths (from top to bottom) are W1,W2,W3.
Ada's strength is S. Whenever she hits a stack of bricks, consider the largest k≥0 such that the sum of widths of the topmost k bricks does not exceed S; the topmost k bricks break and are removed from the stack. Before each hit, Ada may also decide to reverse the current stack of bricks, with no cost.
Find the minimum number of hits Ada needs in order to break all bricks if she performs the reversals optimally. You are not required to minimise the number of reversals.
Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains four space-separated integers S, W1, W2 and W3.Output
For each test case, print a single line containing one integer ― the minimum required number of hits.Constraints
- 1≤T≤64
- 1≤S≤8
- 1≤Wi≤2 for each valid i
it is guaranteed that Ada can break all bricksExample Input

3

3 1 2 2

2 1 1 1

3 2 2 1
Example Output

2

2

2
Explanation

Example case 1:

Ada can reverse the stack and then hit it two times. Before the first hit, the widths of bricks in the stack (from top to bottom) are (2,2,1). After the first hit, the topmost brick breaks and the stack becomes (2,1). The second hit breaks both remaining bricks.

In this particular case, it is also possible to hit the stack two times without reversing. Before the first hit, it is (1,2,2). The first hit breaks the two bricks at the top (so the stack becomes (2)) and the second hit breaks the last brick.
"""

def min_hits_to_break_bricks(S, W1, W2, W3):
    # List of brick widths
    W = [W1, W2, W3]
    
    # Reverse the list to simulate optimal reversal
    W = W[::-1]
    
    hits = 0
    i = 0
    
    while i < len(W):
        k = i
        su = 0
        
        # Sum up the widths until the sum exceeds S or we reach the end of the list
        while k < len(W) and su + W[k] <= S:
            su += W[k]
            k += 1
        
        # Increment the hit counter
        hits += 1
        
        # Move to the next set of bricks
        i = k
    
    return hits