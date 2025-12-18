"""
QUESTION:
In Japan, temperature is usually expressed using the Celsius (℃) scale. In America, they used the Fahrenheit (℉) scale instead. $20$ degrees Celsius is roughly equal to $68$ degrees Fahrenheit. A phrase such as "Today’s temperature is $68$ degrees" is commonly encountered while you are in America.

A value in Fahrenheit can be converted to Celsius by first subtracting $32$ and then multiplying by $\frac{5}{9}$. A simplified method may be used to produce a rough estimate: first subtract $30$ and then divide by $2$. Using the latter method, $68$ Fahrenheit is converted to $19$ Centigrade, i.e., $\frac{(68-30)}{2}$.

Make a program to convert Fahrenheit to Celsius using the simplified method: $C = \frac{F - 30}{2}$.



Input

The input is given in the following format.


$F$


The input line provides a temperature in Fahrenheit $F$ ($30 \leq F \leq 100$), which is an integer divisible by $2$.

Output

Output the converted Celsius temperature in a line.

Examples

Input

68


Output

19


Input

50


Output

10
"""

def fahrenheit_to_celsius(fahrenheit: int) -> int:
    """
    Converts a temperature from Fahrenheit to Celsius using a simplified method.

    Parameters:
    fahrenheit (int): The temperature in Fahrenheit, within the range 30 <= fahrenheit <= 100 and divisible by 2.

    Returns:
    int: The temperature in Celsius.
    """
    return (fahrenheit - 30) // 2