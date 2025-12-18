"""
QUESTION:
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.



Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion. 



Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.



Example 1:

Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]



Note:

The number of given pairs will be in the range [1, 1000].
"""

def find_longest_chain(pairs):
    # Sort pairs based on the second element of each pair
    pairs = sorted(pairs, key=lambda x: x[1])
    
    # Initialize the result and the first pair in the chain
    res = 1
    first = pairs[0]
    
    # Iterate through the pairs starting from the second pair
    for i in pairs[1:]:
        # If the current pair can follow the previous pair, update the chain
        if first[-1] < i[0]:
            res += 1
            first = i
    
    return res