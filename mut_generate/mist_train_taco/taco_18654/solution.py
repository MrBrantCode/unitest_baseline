"""
QUESTION:
A sequence a_1,a_2,... ,a_n is said to be /\/\/\/ when the following conditions are satisfied:

* For each i = 1,2,..., n-2, a_i = a_{i+2}.
* Exactly two different numbers appear in the sequence.



You are given a sequence v_1,v_2,...,v_n whose length is even. We would like to make this sequence /\/\/\/ by replacing some of its elements. Find the minimum number of elements that needs to be replaced.

Constraints

* 2 \leq n \leq 10^5
* n is even.
* 1 \leq v_i \leq 10^5
* v_i is an integer.

Input

Input is given from Standard Input in the following format:


n
v_1 v_2 ... v_n


Output

Print the minimum number of elements that needs to be replaced.

Examples

Input

4
3 1 3 2


Output

1


Input

6
105 119 105 119 105 119


Output

0


Input

4
1 1 1 1


Output

2
"""

def min_replacements_to_v_sequence(n, sequence):
    # Initialize frequency arrays for odd and even indexed elements
    odd_freq = [[0, i] for i in range(100001)]
    even_freq = [[0, i] for i in range(100001)]
    
    # Count frequencies of elements at odd and even indices
    for i in range(n // 2):
        odd_freq[sequence[i * 2]][0] += 1
        even_freq[sequence[i * 2 + 1]][0] += 1
    
    # Sort the frequency arrays in descending order
    odd_freq.sort(reverse=True)
    even_freq.sort(reverse=True)
    
    # Initialize the result with a large number
    res = 10000000000000000
    
    # Find the minimum replacements needed
    for i in range(2):
        for j in range(2):
            if odd_freq[i][1] != even_freq[j][1]:
                res = min(res, n - odd_freq[i][0] - even_freq[j][0])
    
    return res