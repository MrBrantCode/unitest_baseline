"""
QUESTION:
Chef has a binary array in an unsorted manner. Cheffina challenges chef to find the transition point in the sorted (ascending) binary array. Here indexing is starting from 0.
Note: Transition point always exists.

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains two lines of input, $N$.
- N space-separated binary numbers. 

-----Output:-----
For each test case, output in a single line answer.

-----Constraints-----
- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$

-----Sample Input:-----
1
5
0 1 0 0 1

-----Sample Output:-----
3

-----EXPLANATION:-----
binary array in sorted form will look like = [0, 0, 0, 1, 1]
"""

def find_transition_point(binary_array):
    # Sort the binary array
    sorted_array = sorted(binary_array)
    
    # Find the transition point
    for i in range(len(sorted_array)):
        if sorted_array[i] == 1:
            return i

    # If no transition point is found (though the problem guarantees it exists)
    return -1