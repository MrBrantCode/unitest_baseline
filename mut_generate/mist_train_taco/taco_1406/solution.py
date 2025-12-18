"""
QUESTION:
Ted: Robin, get me my legal pad. It's Pros and Cons Time!

There is a long list of n girls in front of Barney, and he is to calculate the optimal "happiness" he can find by selecting exactly 2 girls. (Why 2? No one knows!)

Ted, as a fan of pros and cons, suggests to make a list, a method for estimating the maximum happiness that Barney can achieve. 

Each girl is characterized by two parameters:

- favour: if this girl is chosen, his happiness increases by this amount. 
- anger: if this girl is not chosen, his happiness decreases by this amount.

Find the maximum "happiness" that Barney can obtain. Note that the answer is allowed to be negative.

Input:
The first line of input file contains an integer t, denoting the number of test cases to follow.

The first line of each test case contains an integer n, as explained in statement.
It is followed by n lines, each containing two space-seperated integers denoting the favour and anger of the ith girl.

Output:
The output file should contain t lines, each containing answer for the test case.

Constraints:
1 ≤ t ≤ 10
2 ≤ n ≤ 1e5
0 ≤ favour[i], anger[i] ≤ 1e9
None of the input files exceed 4MB.

SAMPLE INPUT
1
4
2 3
10 2
11 5
4 1

SAMPLE OUTPUT
17

Explanation

Choose girl 2 and 3
happiness = 10 + 11 - 1 - 3 = 17
"""

def calculate_maximum_happiness(test_cases):
    def HQ(h, a, A):
        return h + a - float(A) / 2

    results = []
    
    for case in test_cases:
        n = len(case)
        list_a = case
        
        A = sum([i[1] for i in list_a])
        H = sorted([HQ(i[0], i[1], A) for i in list_a], reverse=True)
        
        results.append(int(H[0] + H[1]))
    
    return results