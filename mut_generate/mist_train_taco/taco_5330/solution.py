"""
QUESTION:
Chef hates unoptimized codes and people who write such codes. One fine day he decided to look through the kitchen's codebase and found a function whose pseudo-code is given here:

input: integer N, list X[1, 2, ..., N], list Y[1, 2, ..., N]

output: integer res

function:

set res = 0;
for i := 1 to N do
for j := 1 to N do
for k := 1 to N do
if (X[i] = X[j]) OR (X[j] = X[k]) OR (X[k] = X[i])
continue
else
set res = max(res, Y[i] + Y[j] + Y[k])
return res

Luckily enough this code gets triggered only if the Head Chef makes a submission. But still there is a possibility that this can crash the judge. So help Chef by writing a new function which does the same thing but is faster.

-----Input-----
- The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains an integer N denoting the number of elements in the two lists.
- The i-th of the next N lines contains a pair of space-separated integers denoting the values of X[i] and Y[i] respectively.

-----Output-----
For each test case, output an integer corresponding to the return value of the function.

-----Constraints-----
- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 105
- 1 ≤ X[i], Y[i] ≤ 108

-----Example-----
Input
2
3
1 3
3 1
1 2
5
1 3
2 4
1 2
3 2
3 4

Output
0
11

-----Explanation-----
Testcase 2: The maximum is attained when i = 1, j = 2 and k = 5. This leads to res being 3 + 4 + 4 = 11. This value is attained in other iterations as well, but it never exceeds this, and hence this is the answer.
"""

def find_max_sum_of_distinct_x_values(test_cases):
    results = []
    
    for case in test_cases:
        N = case['N']
        pairs = case['pairs']
        
        # Dictionary to store the maximum Y value for each distinct X
        x_to_max_y = {}
        
        for x, y in pairs:
            if x in x_to_max_y:
                x_to_max_y[x] = max(x_to_max_y[x], y)
            else:
                x_to_max_y[x] = y
        
        # If there are less than 3 distinct X values, the result is 0
        if len(x_to_max_y) < 3:
            results.append(0)
        else:
            # Get the values of Y for distinct X and sort them
            y_values = list(x_to_max_y.values())
            y_values.sort()
            
            # The result is the sum of the three largest Y values
            results.append(y_values[-1] + y_values[-2] + y_values[-3])
    
    return results