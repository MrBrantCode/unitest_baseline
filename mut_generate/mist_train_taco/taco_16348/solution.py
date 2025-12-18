"""
QUESTION:
Gotham City is again under attack. This time Joker has given an open challenge to solve the following problem in order to save Gotham. Help Batman in protecting Gotham by solving the problem.
You are given two strings A and B composed of lowercase letters of Latin alphabet. B can be obtained by removing some characters from A(including 0). You are given an array containing any random permutation of numbers $1$ to $N$, where $N$ is the length of the string A. You have to remove the letters of A in the given order of indices. Note that after removing one letter, the indices of other letters do not change. Return the maximum number of indices you can remove in the given order such that B is still obtainable from A.

-----Input:-----
- First two lines contains the strings A and B respectively.
- The third line contains a random permutation of numbers from $1$ to $N$ representing some order of indices of string A.

-----Output:-----
Print a single number denoting the maximum number of indices you can remove in the given order such that B is still obtainable from A.

-----Constraints-----
- $1 \leq |B| \leq |A| \leq 200000$

-----Sample Input #1:-----
xxyxxy
xyy
1 5 4 6 3 2

-----Sample Output #1:-----
3

-----Sample Input #2:-----
jphokenixr
joker
2 9 3 7 8 1 6 5 4 10

-----Sample Output #2:-----
5

-----EXPLANATION:-----
For the first example removing characters in order,
xxyxxy => _xyxxy => _xyx_y => _xy__y.
If we remove any other element now then we can not obtain 'xxy'. So the ans is 3.
"""

def max_removals_to_obtain_b(A: str, B: str, indices: list[int]) -> int:
    # Convert A to a list for easier manipulation
    A_list = list(A)
    # Create a set of characters in B for quick lookup
    B_set = set(B)
    # Initialize a counter for the number of removals
    removals = 0
    
    # Iterate over the indices in the given order
    for index in indices:
        # Adjust index to be 0-based
        index -= 1
        # Check if removing the character at this index still allows B to be obtained
        if A_list[index] in B_set:
            # Remove the character from the set of characters in B
            B_set.remove(A_list[index])
        # Increment the removal counter
        removals += 1
        # If B_set is empty, we have removed enough characters to obtain B
        if not B_set:
            break
    
    # The maximum number of removals is the total length of A minus the length of B
    max_removals = len(A) - len(B)
    # Return the minimum of the calculated removals and the maximum possible removals
    return min(removals, max_removals)