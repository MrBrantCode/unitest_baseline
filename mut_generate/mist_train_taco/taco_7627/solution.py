"""
QUESTION:
Many things in this first paragraph are references to some pretty famous YouTube stars, so be careful about rephrasing. Thanks! 
Michael, Kevin and Jake are sharing a cake, in celebration of their Webby award. They named it VCake. Unlike other cakes they considered, this one has finite volume and surface area. It's shaped as a normal rectangular cake with dimensions R centimeters by C centimeters. For the purposes of this problem, we can forget about three dimensions and think of a cake as just a 2D rectangle.
Chef will now cut the cake into three pieces, one for each person. However, the cake's shape and Chef's really old tools pose a few restrictions:

- Chef can only cut the cake, or a cake piece, across a line parallel to one of its sides. 
- Chef can only cut the cake, or a cake piece, from end to end. That is, she cannot cut the cake partially. 
- Chef can only cut the cake, or a cake piece, such that the sides of the resulting pieces (which will be rectangular in shape) are integers. 

In addition, Michael, Kevin and Jake also have a few preferences of their own:

- They want their pieces to be connected (in one piece), and rectangular in shape.
- Michael wants his piece to have an area exactly M square centimeters. (Again, forget about a third dimension.)
- Kevin wants his piece to have an area exactly K square centimeters.
- Jake wants his piece to have an area exactly J square centimeters.

With these restrictions, Chef is at a loss. Is it possible for Chef to accomplish this task? Please note that the entire cake should be used. There should be no leftover cake.

-----Input-----
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
Each test case consists of a single line containing five space separated integers R, C M, K and J.

-----Output-----
For each test case, output a single line containing either “Yes” or “No” (without quotes), denoting whether Chef can accomplish the task or not.

-----Constraints-----
- 1 ≤ T ≤ 105
- 1 ≤ R, C ≤ 109
- 1 ≤ M, K, J ≤ 1018

-----Example-----
Input:4
4 5 10 4 6
4 5 6 10 4
4 5 4 6 10
2 2 2 2 2

Output:Yes
Yes
Yes
No

-----Explanation-----
Example case 1. In this case, Chef can accomplish the task by doing the following slicing.  
pre tt
_ _ _ _ _       _ _ _ _ _       _ _ _ _ _       _________ 
|         |     |         |     |         |     |M M M M M|
|         | -- |_ _ _ _ _| -- |_ _ _ _ _| -- |M_M_M_M_M|
|         |     |         |     |     |   |     |J J J|K K|
|_ _ _ _ _|     |_ _ _ _ _|     |_ _ _|_ _|     |J_J_J|K_K|
/tt /pre
I'll make an image if I have time 
Example case 4. Here, Michael, Kevin and Jake each wants a piece with area 2, but the total area of the cake is only 2×2 = 4. This means the task is impossible.
"""

def can_cut_cake(R, C, M, K, J):
    # Check if the total area matches the sum of the desired areas
    if R * C != M + K + J:
        return False
    
    # List of all permutations of M, K, J
    areas = [(M, K, J), (M, J, K), (K, M, J), (K, J, M), (J, M, K), (J, K, M)]
    
    for m, k, j in areas:
        # Check if m can be a valid piece by cutting along rows
        if m % R == 0:
            c_remain_1 = C - m // R
            if k % R == 0:
                c_remain_2 = c_remain_1 - k // R
                if c_remain_2 * R == j:
                    return True
            if k % c_remain_1 == 0:
                r_remain_2 = R - k // c_remain_1
                if r_remain_2 * c_remain_1 == j:
                    return True
            if j % R == 0:
                c_remain_2 = c_remain_1 - j // R
                if c_remain_2 * R == k:
                    return True
            if j % c_remain_1 == 0:
                r_remain_2 = R - j // c_remain_1
                if r_remain_2 * c_remain_1 == k:
                    return True
        
        # Check if m can be a valid piece by cutting along columns
        if m % C == 0:
            r_remain_1 = R - m // C
            if k % r_remain_1 == 0:
                c_remain_2 = C - k // r_remain_1
                if c_remain_2 * r_remain_1 == j:
                    return True
            if k % C == 0:
                r_remain_2 = r_remain_1 - k // C
                if r_remain_2 * C == j:
                    return True
            if j % r_remain_1 == 0:
                c_remain_2 = C - j // r_remain_1
                if c_remain_2 * r_remain_1 == k:
                    return True
            if j % C == 0:
                r_remain_2 = r_remain_1 - j // C
                if r_remain_2 * C == k:
                    return True
    
    return False