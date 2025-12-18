"""
QUESTION:
There is a double-track line (up and down are separate lines and pass each other everywhere). There are 11 stations on this line, including the terminal station, and each station is called by the section number shown in the figure.

<image>


Trains depart from both terminal stations on this line at the same time and run without stopping along the way. Create a program that reads the length of each section and the speed of the two trains and outputs the number of the section where the trains pass each other in each case. However, if you pass each other just at the station, the smaller number of the section numbers on both sides will be output. In addition, the length of the train and the length of the station cannot be ignored.



Input

Multiple datasets are given. Each dataset is given in the following format.


l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, v1, v2


li (1 ≤ li ≤ 2,000) is an integer representing the length (km) of the interval i. v1 is the speed of the train departing from the terminal station on the section 1 side (km / h), and v2 is the speed of the train departing from the terminal station on the section 10 side (km / h) (1 ≤ v1, v2) ≤ 2,000).

The number of datasets does not exceed 50.

Output

For each data set, the number of the section where the train passes is output on one line.

Example

Input

1,1,1,1,1,1,1,1,1,1,40,60
1,1,1,1,1,3,3,3,3,3,50,50
10,10,10,10,10,10,10,10,10,10,50,49


Output

4
7
6
"""

def find_passing_section(sections, v1, v2):
    """
    Finds the section number where two trains pass each other on a double-track line.

    Parameters:
    - sections (list of int): A list of integers representing the lengths of each section.
    - v1 (int): Speed of the train departing from the terminal station on the section 1 side.
    - v2 (int): Speed of the train departing from the terminal station on the section 10 side.

    Returns:
    - int: The section number where the trains pass each other.
    """
    total_length = sum(sections)
    kp = total_length * v1 / (v1 + v2)
    
    cumulative_length = 0
    for num, length in enumerate(sections):
        cumulative_length += length
        if cumulative_length >= kp:
            return num + 1