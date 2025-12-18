"""
QUESTION:
As I was cleaning up the warehouse, I found an old document that describes how to get to the treasures of my ancestors. The following was written in this ancient document.


1. First, stand 1m east of the well on the outskirts of the town and turn straight toward the well.
2. Turn clockwise 90 degrees, go straight for 1m, and turn straight toward the well.
3. Turn clockwise 90 degrees, go straight for 1m, and turn straight toward the well.
Four.                   〃
Five.                   〃
6::


From the second line onward, exactly the same thing was written. You wanted to find the treasure, but found it awkward. Unlike in the past, the building is in the way, and you can't see the well even if you go straight in the direction of the well, or you can't go straight even if you try to go straight for 1m. In addition, this ancient document has nearly 1000 lines, and it takes a considerable amount of time and physical strength to work according to the ancient document. Fortunately, however, you can take advantage of your computer.

Enter the number of lines n written in the old document and create a program that outputs the location of the treasure. However, n is a positive integer between 2 and 1,000.



input

Given multiple datasets. For each dataset, one integer n, which represents the number of lines in the old document, is given on each line.

The input ends with -1. The number of datasets does not exceed 50.

output

Assuming that there is a treasure at the position x (m) to the east and y (m) to the north from the well on the outskirts of the town, output each data set in the following format.


x
y


The output is a real number and may contain an error of 0.01 or less.

Example

Input

3
6
-1


Output

0.29
1.71
-2.31
0.80
"""

def calculate_treasure_location(n: int) -> tuple:
    """
    Calculate the location of the treasure based on the number of lines in the ancient document.

    Parameters:
    n (int): The number of lines in the ancient document.

    Returns:
    tuple: A tuple containing the coordinates (x, y) of the treasure.
    """
    MAX = 1005
    r = [0.0] * MAX
    d = [0.0] * MAX
    r[1] = 1.0
    
    for i in range(2, MAX):
        d[i] = d[i - 1] + math.atan(1 / r[i - 1])
        r[i] = math.sqrt(r[i - 1] ** 2 + 1)
    
    x = r[n] * math.cos(d[n])
    y = r[n] * math.sin(d[n])
    
    return (x, y)