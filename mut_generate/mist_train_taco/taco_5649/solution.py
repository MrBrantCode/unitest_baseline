"""
QUESTION:
Problem statement

AOR Ika got a cabbage with $ N $ leaves. The leaves of this cabbage are numbered $ 1, \ ldots, N $ in order from the outside, and the dirtiness of the $ i $ th leaf is $ D_i $. The larger this value is, the worse the degree of dirt is. AOR Ika-chan decided to use the cabbage leaves for cooking, so she decided to select the dirty leaves to be discarded according to the following procedure.

1. Initialize the discard candidates to empty.
2. Focus on the outermost leaves that have not yet been examined. If all the items have been checked, the process ends.
3. If the leaf is dirty for $ A $ or more, add it to the discard candidate and return to 2. Otherwise it ends.



However, as a result of this operation, I noticed that the number of leaves that can be used for cooking may be extremely reduced. Therefore, I decided to reconsider the leaves to be discarded after the above operation and perform the following operations.

1. If there are less than $ M $ leaves that are not candidates for disposal, proceed to 2. Otherwise it ends.
2. Focus on the innermost leaf that has not been examined yet among the leaves that are candidates for disposal. If there are no leaves that are candidates for disposal, the process ends.
3. If the leaf is less than $ B $, remove it from the discard candidates and return to 2. Otherwise, discard all the leaves remaining in the discard candidates and finish.



When you perform these operations, find the number of leaves to be finally discarded.

Input constraints

$ 1 \ leq N \ leq 1000 $
$ 0 \ leq M \ leq N $
$ 1 \ leq A \ leq B \ leq 1000 $
$ 1 \ leq D_ {i} \ leq 1000 $

sample

Sample input 1


5 3 6 9
9 7 5 3 1


Sample output 1


2


Discard the first and second sheets.

Sample input 2


5 3 6 9
5 4 3 2 1


Sample output 2


0


Do not throw away from the first piece.

Sample input 3


5 3 6 9
10 8 6 4 2


Sample output 3


1


I tried to throw away the third one, but I reconsidered and decided not to throw away the second and third ones.

Sample input 4


5 3 6 9
5 10 8 6 4


Sample output 4


0


AOR Ika doesn't know that the second piece is dirty.

Sample input 5


5 0 6 9
9 9 8 8 7


Sample output 5


Five


I don't mind throwing everything away.



input

$ N \ M \ A \ B $
$ D_ {1} \ D_ {2} \ \ cdots \ D_ {N} $

output

Output the number of leaves to be finally thrown away.

Example

Input

5 3 6 9
9 7 5 3 1


Output

2
"""

def calculate_discarded_leaves(n, m, a, b, ds):
    is_waste = [False for _ in range(n)]
    
    # Step 1: Identify initial discard candidates
    for i in range(n):
        if ds[i] >= a:
            is_waste[i] = True
        else:
            break
    
    # Step 2: Reconsider discard candidates if necessary
    if sum(is_waste) > n - m:
        for i in range(n)[::-1]:
            if is_waste[i]:
                if ds[i] <= b:
                    is_waste[i] = False
                else:
                    break
    
    # Return the number of leaves to be discarded
    return sum(is_waste)