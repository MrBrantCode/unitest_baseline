"""
QUESTION:
The Jones Trucking Company tracks the location of each of its trucks on a grid similar to an (x, y) plane. The home office is at the location (0, 0). Read the coordinates of truck A and the coordinates of truck B and determine which is closer to the office.

-----Input:-----
The first line of the data set for this problem is an integer representing the number of collections of data that follow. Each collection contains 4 integers: the x-coordinate and then the 
y-coordinate of truck A followed by the x-coordinate and then the  y-coordinate of truck B.

-----Output:-----
All letters are upper case.
The output is to be formatted exactly like that for the sample output given below.

-----Assumptions:-----
The x-coordinate is in the range –20 .. 20. The y-coordinate is in the range –20 .. 20.

-----Discussion:-----
The distance between point #1 with coordinates (x1, y1) and point #2 with coordinates (x2, y2) is:

-----Sample Input:-----
4
3 -2 -5 -3
0 6 1 2
-7 8 4 -1
3 3 -2 2

-----Sample Output:-----
A IS CLOSER
B IS CLOSER
B IS CLOSER
B IS CLOSER
"""

def determine_closer_truck(truck_a_x: int, truck_a_y: int, truck_b_x: int, truck_b_y: int) -> str:
    """
    Determines which truck (A or B) is closer to the office located at (0, 0).

    Parameters:
    - truck_a_x (int): The x-coordinate of truck A.
    - truck_a_y (int): The y-coordinate of truck A.
    - truck_b_x (int): The x-coordinate of truck B.
    - truck_b_y (int): The y-coordinate of truck B.

    Returns:
    - str: A string indicating which truck is closer. The possible values are "A IS CLOSER" or "B IS CLOSER".
    """
    distance_a = truck_a_x ** 2 + truck_a_y ** 2
    distance_b = truck_b_x ** 2 + truck_b_y ** 2
    
    if distance_a > distance_b:
        return "B IS CLOSER"
    else:
        return "A IS CLOSER"