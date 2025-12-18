"""
QUESTION:
Given length l, width b and height h of a cuboid. Find the total surface area and volume of cuboid.
 
Example 1:
Input: l = 1, b = 2, h = 3
Output: 22 6
Explanation: Surface area = 2 * (2 * 3
+ 3 * 1 + 1 * 2) = 22 and volume = 
1 * 2 * 3 = 6
Example 2:
Input: l = 2, b = 3, h = 5
Output: 62 30
Explanation: Surface area = 2 * (3 * 5
+ 5 * 2 + 2 * 3) = 62 and volume = 
2 * 3 * 5 = 30
 
Your Task:
You don't need to read or print anything. Your task is to complete the function find() which takes l, b and h as input parameter and returns a list containing the value of surface area and volume.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
 
Costraints:
1 <= l, b, h <= 10^{6}
"""

def calculate_cuboid_properties(l: int, b: int, h: int) -> tuple:
    """
    Calculate the total surface area and volume of a cuboid.

    Parameters:
    l (int): Length of the cuboid.
    b (int): Breadth of the cuboid.
    h (int): Height of the cuboid.

    Returns:
    tuple: A tuple containing the total surface area and volume of the cuboid.
    """
    volume = l * b * h
    surface_area = 2 * (l * b + b * h + h * l)
    return (surface_area, volume)