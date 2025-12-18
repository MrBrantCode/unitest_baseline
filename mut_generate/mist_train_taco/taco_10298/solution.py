"""
QUESTION:
On a wall, there are C circles. You need to connect various circles using straight lines so that the resulting figure is a planar graph with exactly F faces.  Print the units digit of number of edges we can draw between various circles so as the resulting graph is planar with F faces. 
Note: C and F can be very large. So, C and F are taken as String Input.
 
Example 1:
Input:
C = "6" , F = "10"
Output:
4
Explanation:
14 edges will be needed. Unit digit
of 14 is 4. So,Output is 4.
Example 2:
Input:
C = "100" , F = "667"
Output:
5
Explanation:
765 edges will be needed. Unit digit
of 765 is 5. So,Output is 5.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function findNoOfEdges() which takes Strings C and F as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= C,F <= 10^{10000}
"""

def findNoOfEdges(C: str, F: str) -> int:
    # Convert the input strings to integers
    C_int = int(C)
    F_int = int(F)
    
    # Calculate the number of edges using the formula
    edges = C_int + F_int - 2
    
    # Get the units digit of the number of edges
    units_digit = edges % 10
    
    return units_digit