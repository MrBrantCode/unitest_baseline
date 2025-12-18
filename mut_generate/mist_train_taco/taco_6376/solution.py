"""
QUESTION:
We have N voting papers. The i-th vote (1 \leq i \leq N) has the string S_i written on it.
Print all strings that are written on the most number of votes, in lexicographical order.

-----Constraints-----
 - 1 \leq N \leq 2 \times 10^5
 - S_i (1 \leq i \leq N) are strings consisting of lowercase English letters.
 - The length of S_i (1 \leq i \leq N) is between 1 and 10 (inclusive).

-----Input-----
Input is given from Standard Input in the following format:
N
S_1
:
S_N

-----Output-----
Print all strings in question in lexicographical order.

-----Sample Input-----
7
beat
vet
beet
bed
vet
bet
beet

-----Sample Output-----
beet
vet

beet and vet are written on two sheets each, while beat, bed, and bet are written on one vote each. Thus, we should print the strings beet and vet.
"""

def find_most_frequent_votes(votes):
    """
    Finds and returns all strings that are written on the most number of votes, 
    in lexicographical order.

    Parameters:
    votes (list of str): A list of strings representing the voting papers.

    Returns:
    list of str: A list of strings that are written on the most number of votes, 
                 sorted in lexicographical order.
    """
    D = {}
    M = 1
    
    # Count the frequency of each string
    for S in votes:
        if S in D:
            D[S] += 1
            M = max(M, D[S])
        else:
            D[S] = 1
    
    # Find all strings with the maximum frequency
    K = [a for a in D if D[a] == M]
    
    # Sort the strings lexicographically
    K.sort()
    
    return K