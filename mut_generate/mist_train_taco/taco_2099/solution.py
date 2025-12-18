"""
QUESTION:
We have five variables x_1, x_2, x_3, x_4, and x_5.
The variable x_i was initially assigned a value of i.
Snuke chose one of these variables and assigned it 0.
You are given the values of the five variables after this assignment.
Find out which variable Snuke assigned 0.

-----Constraints-----
 - The values of x_1, x_2, x_3, x_4, and x_5 given as input are a possible outcome of the assignment by Snuke.

-----Input-----
Input is given from Standard Input in the following format:
x_1 x_2 x_3 x_4 x_5

-----Output-----
If the variable Snuke assigned 0 was x_i, print the integer i.

-----Sample Input-----
0 2 3 4 5

-----Sample Output-----
1

In this case, Snuke assigned 0 to x_1, so we should print 1.
"""

def find_zero_assigned_variable(x1, x2, x3, x4, x5):
    # Create a list of the input values
    values = [x1, x2, x3, x4, x5]
    
    # Iterate through the list to find the index of the value that is 0
    for i in range(len(values)):
        if values[i] == 0:
            # Return the 1-based index
            return i + 1

# Example usage:
# result = find_zero_assigned_variable(0, 2, 3, 4, 5)
# print(result)  # Output: 1