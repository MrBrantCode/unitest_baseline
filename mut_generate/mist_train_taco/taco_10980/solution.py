"""
QUESTION:
Given a temperature in celsius C. You have to convert it in Fahrenheit.
 
Example 1:
Input:
C = 32
Output:
89.60
Explanation:
For 32 degree C temperature 
in farenheit = 89.60
Example 2:
Input:
C = 25
Output:
77.00
Explanation:
For 25 degree C temperature 
in farenheit = 77.
Your Task:
You don't need to read input or print anything. Your task is to complete the function celciusToFahrenheit() which takes an integer C as input parameters and returns a float value, after converting it into Fahrenheit.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
 
Constraints:
1 <= C <= 100000
"""

def celsius_to_fahrenheit(C: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit.

    Parameters:
    C (float): The temperature in Celsius.

    Returns:
    float: The temperature in Fahrenheit.
    """
    return C * 9 / 5 + 32