"""
QUESTION:
Given a string S on which you need to perform Q replace operations.
Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y. The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y. If not, we do nothing.
Note:  All these operations occur simultaneously. It's guaranteed that there won't be any overlap in replacement: for example, S = "abc", indexes = [0,1], sources = ["ab", "bc"] is not a valid test case. 
Example 1:
Input: 
S = "gforks"
Q = 2
index[] = {0, 4}
sources[] = {"g", "ks"}
targets[] = {"geeks", "geeks"}
Output: 
geeksforgeeks
Explanation:
"g" starts at index 0, so, it's replaced by
"geeks". Similarly, "ks" starts at index 4,
and is replaced by "geeks".
Example 2:
Input: 
S = "gforks"
Q = 2
index[] = {0, 3}
sources[] = {"g", "ss"}
targets[] = {"geeks", "geeks"}
Output: 
geeksforks
Explanation:
"g" starts at index 0, so, it's replaced by
"geeks". "ss" doesn't start at index 3 in
original S, so it's not replaced.
Your Task:
You don't need to read input or print anything. You only need to complete the function findAndReplace() that takes a string S, an integer Q, and 3 arrays index, sources, and targets of size Q, as input and returns the new string after all the operations. index[i], sources[i], and targets[i] denotes the index, sources, and targets for i_{th} query.
Expected Time Complexity:  O(|S| * Q)
Expected Auxilliary Space: O(Q)
 
Constraints:
1 ≤ |S| ≤ 10^{4}
1 ≤ Q ≤ 100
1 ≤ length of sources_{i}, targets_{i} ≤ 100
"""

def find_and_replace(S, Q, index, sources, targets):
    # Create a list of replacements with their corresponding indices, sources, and targets
    replacements = [(index[i], sources[i], targets[i]) for i in range(Q)]
    
    # Sort the replacements in reverse order to handle the replacements from the end to the start
    replacements.sort(reverse=True)
    
    # Perform the replacements
    for (i, source, target) in replacements:
        if S[i:i + len(source)] == source:
            S = S[:i] + target + S[i + len(source):]
    
    return S