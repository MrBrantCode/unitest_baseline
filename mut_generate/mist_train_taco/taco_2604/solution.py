"""
QUESTION:
A sequence a_1,a_2,... ,a_n is said to be /\/\/\/ when the following conditions are satisfied:
 - For each i = 1,2,..., n-2, a_i = a_{i+2}.
 - Exactly two different numbers appear in the sequence.
You are given a sequence v_1,v_2,...,v_n whose length is even.
We would like to make this sequence /\/\/\/ by replacing some of its elements.
Find the minimum number of elements that needs to be replaced.

-----Constraints-----
 - 2 \leq n \leq 10^5
 - n is even.
 - 1 \leq v_i \leq 10^5
 - v_i is an integer.

-----Input-----
Input is given from Standard Input in the following format:
n
v_1 v_2 ... v_n

-----Output-----
Print the minimum number of elements that needs to be replaced.

-----Sample Input-----
4
3 1 3 2

-----Sample Output-----
1

The sequence 3,1,3,2 is not /\/\/\/, but we can make it /\/\/\/ by replacing one of its elements: for example, replace the fourth element to make it 3,1,3,1.
"""

def min_replacements_to_v_sequence(n, v):
    # Initialize counters for odd and even indexed elements
    odd = [0] * (10 ** 5 + 5)
    even = [0] * (10 ** 5 + 5)
    
    # Count occurrences of each element at odd and even indices
    for i in range(n):
        if i % 2 == 0:
            even[v[i]] += 1
        else:
            odd[v[i]] += 1
    
    # Calculate the total number of elements in odd and even positions
    sum_odd = sum(odd)
    sum_even = sum(even)
    
    # Initialize the answer with the total number of elements
    ans = sum_odd + sum_even
    
    # Find the maximum occurrences in odd and even positions
    max_odd = max(odd)
    max_even = max(even)
    
    # If the most frequent elements in odd and even positions are different
    if odd.index(max_odd) != even.index(max_even):
        return sum_odd + sum_even - max_even - max_odd
    else:
        # Sort the counts to find the second most frequent elements
        odd.sort()
        even.sort()
        
        # Determine the best way to minimize replacements
        if odd[-1] - odd[-2] > even[-1] - even[-2]:
            ans -= odd[-1] + even[-2]
        else:
            ans -= odd[-2] + even[-1]
    
    return ans