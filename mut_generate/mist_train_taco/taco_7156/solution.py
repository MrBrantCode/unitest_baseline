"""
QUESTION:
The chef is playing a game of long distance. Chef has a number K and he wants to find the longest distance between the index of the first and the last occurrence of K in a given array of N numbers.

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains two lines of input.
- Next line with Two integers in one line $K, N$.
- Next line with $N$ space-separated integers.

-----Output:-----
For each test case, output in a single line answer as the index of first and last occurrence of K in the given array.
Note: Here Indexing is from 1 not  0 based.

-----Constraints-----
- $1 \leq T \leq 100$
- $1 \leq k \leq 10^5$
- $1 \leq N \leq 10^5$

-----Sample Input:-----
2
2 6
2 3 4 2 1 6
4 6
2 3 4 2 1 6

-----Sample Output:-----
3
0

-----EXPLANATION:-----
For 1) Index of First and last occurrence of 2 in the given array is at 1 and 4, i.e. distance is 3. 
For 2) 4 occurs only once in the given array hence print 0.
"""

def find_longest_distance(K, N, array):
    # Initialize the last occurrence index to -1
    last_index = -1
    
    # Traverse the array from the end to find the last occurrence of K
    for i in range(N - 1, -1, -1):
        if array[i] == K:
            last_index = i
            break
    
    # Initialize the first occurrence index to -1
    first_index = -1
    
    # Traverse the array from the start to find the first occurrence of K
    for i in range(N):
        if array[i] == K:
            first_index = i
            break
    
    # Calculate the distance between the first and last occurrence
    if first_index == -1 or last_index == -1:
        return 0
    else:
        # Convert to 1-based index and return the distance
        return (last_index + 1) - (first_index + 1)