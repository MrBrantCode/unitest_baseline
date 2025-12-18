"""
QUESTION:
You are given a spreadsheet that contains a list of $N$ athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the $K^{th}$ attribute and print the final resulting table. Follow the example given below for better understanding. 

Note that $\mbox{K}$ is indexed from $\mbox{0}$ to $M-1$, where $\mbox{M}$ is the number of attributes. 

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

Input Format

The first line contains $N$ and $\mbox{M}$ separated by a space. 

The next $N$ lines each contain $\mbox{M}$ elements. 

The last line contains $\mbox{K}$.     

Constraints

$1\leq N,M\leq1000$ 

$0\leq K<M$ 

Each element $\leq1000$

Output Format

Print the $N$ lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.   

Sample Input 0
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output 0
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

Explanation 0

The details are sorted based on the second attribute, since $\mbox{K}$ is zero-indexed.
"""

def sort_athletes_by_attribute(n, m, athletes, k):
    """
    Sorts a list of athletes based on the k-th attribute.

    Parameters:
    - n (int): Number of athletes.
    - m (int): Number of attributes per athlete.
    - athletes (list of lists of int): List of athletes where each athlete is represented by a list of attributes.
    - k (int): The index of the attribute to sort by.

    Returns:
    - list of lists of int: The sorted list of athletes.
    """
    athletes.sort(key=lambda x: x[k])
    return athletes