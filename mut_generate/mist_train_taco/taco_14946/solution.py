"""
QUESTION:
<image>


Arrange integers (0 or more and 99 or less) in a rhombus as illustrated in Fig. 1. Create a program that reads the data representing the rhombus and outputs the maximum value of the sum of the integers that pass when starting from the top and proceeding to the bottom according to the following rules.

* At each step, you can proceed to the lower left diagonal or the lower right diagonal.



For example, in the example of Fig. 1, as shown in Fig. 2, when 7,3,8,7,5,7,8,3,7 is selected and passed, the sum is the maximum 55 (7 + 3 + 8). + 7 + 5 + 7 + 8 + 3 + 7 = 55).



Input

As shown in the input example, a comma-separated sequence of integers is given to the diamond. Each line does not contain whitespace. The input example corresponds to Fig. 1. There are less than 100 rows of data.

Output

Outputs the maximum value of the sum of integers that pass according to the rules on one line.

Example

Input

7
3,8
8,1,0
2,7,4,4
4,5,2,6,5
2,7,4,4
8,1,0
3,8
7


Output

55
"""

def max_rhombus_path_sum(rhombus):
    # Copy the input to avoid modifying the original data
    s = [row[:] for row in rhombus]
    
    # Iterate through each row starting from the second row
    for i in range(1, len(s)):
        for j in range(len(s[i])):
            # Determine the range of possible values from the previous row
            t = j - (len(s[i]) > len(s[i - 1]))
            # Update the current value by adding the maximum possible value from the previous row
            s[i][j] += max(s[i - 1][t * (j > 0):t + 2])
    
    # The maximum sum will be the maximum value in the last row
    return max(s[-1])