"""
QUESTION:
There is a carpet of a size a*b [length * breadth]. You are given a box of size c*d. The task is, one has to fit the carpet in the box in a minimum number of moves. 
In one move, you can either decrease the length or the breadth of the carpet by half (floor value of its half).
Note: One can even turn the carpet by 90 degrees any number of times, wont be counted as a move.
 
Example 1:
Input:
A = 8, B = 13
C = 6, D = 10
Output:
Minimum number of moves: 1
Explanation:
Fold the carpet by breadth, 13/2 i.e. 6, 
so now carpet is 6*8 and can fit fine.
 
Example 2:
Input:
A = 4, B = 8
C = 3, D = 10
Output:
Minimum number of moves: 1
Explanation: Fold the carpet by length , 4/2 i.e. 2,
so now carpet is 2*8 and can fit fine.
 
Your Task:
You don't need to read input or print anything. You only need to complete the function carpetBox() that takes an integer A, B, C and D as input and returns an integer denoting the minimum numbers of moves required to fit the carpet into the box.
 
Expected Time Complexity: O( max( log(a), log(b) ) ) .
Expected Auxiliary Space: O(1) .
 
Constrains:
1<= A,B,C,D <= 10^{9}
"""

def carpet_box(A: int, B: int, C: int, D: int) -> int:
    count = 0
    max_cd = max(C, D)
    min_cd = min(C, D)
    max_ab = max(A, B)
    min_ab = min(A, B)
    
    while max_ab > max_cd or min_ab > min_cd:
        if max_ab > max_cd and max_ab == A:
            A //= 2
        elif max_ab > max_cd and max_ab == B:
            B //= 2
        elif min_ab > min_cd and min_ab == A:
            A //= 2
        elif min_ab > min_cd and min_ab == B:
            B //= 2
        count += 1
        max_ab = max(A, B)
        min_ab = min(A, B)
    
    return count