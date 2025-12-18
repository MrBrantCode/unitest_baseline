"""
QUESTION:
Ronny the robot is watching someone perform the Cups and Balls magic trick. The magician has one ball and three cups, he shows Ronny which cup he hides the ball under (b), he then mixes all the cups around by performing multiple two-cup switches (arr). Ronny can record the switches but can't work out where the ball is. Write a programme to help him do this. 

Rules: 
- There will only ever be three cups.
- Only two cups will be swapped at a time. 
- The cups and their switches will be refered to by their index in a row of three, beginning at one. So [[1,2]] means the cup at position one, is swapped with the cup at position two. 
- Arr will be an array of integers 1 - 3 organised in pairs. 
- There won't be any empty sub-arrays.
- If arr is just an empty array b should be returned.

Examples: 

(b) = 2, 
(arr) = [[1,2]]

The ball is under cup number : 1

-------

(b) = 1, 
(arr) = [[2,3],[1,2],[1,2]]

The ball is under cup number : 1

-------

(b) = 2, 
(arr) = [[1,3],[1,2],[2,1],[2,3]]

The ball is under cup number : 3
"""

def find_ball_position(b, arr):
    # Iterate through each swap in the array
    for swap in arr:
        # If the ball is in one of the cups being swapped, update its position
        if b == swap[0]:
            b = swap[1]
        elif b == swap[1]:
            b = swap[0]
    # Return the final position of the ball
    return b