"""
QUESTION:
There is data that records the altitude of mountains that have been climbed so far. Create a program that reads this data and outputs the elevation difference between the highest and lowest mountains.



Input

The input is given in the following format:


Mountain height
...
...


The height of the mountain is given over multiple lines. All values ​​entered are real numbers greater than or equal to 0 and less than or equal to 1,000,000. The number of mountain heights entered is 50 or less.

Output

The elevation difference between the highest mountain and the lowest mountain is output as a real number. The output may contain an error of 0.01 or less.

Example

Input

3776.0
1819.0
645.2
2004.1
1208.6


Output

3130.8
"""

def calculate_elevation_difference(mountain_heights):
    """
    Calculate the elevation difference between the highest and lowest mountains.

    Parameters:
    mountain_heights (list of float): A list of mountain heights.

    Returns:
    float: The elevation difference between the highest and lowest mountains.
    """
    if not mountain_heights:
        return 0.0  # Return 0.0 if the list is empty to avoid errors
    
    min_height = min(mountain_heights)
    max_height = max(mountain_heights)
    
    return max_height - min_height