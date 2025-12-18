"""
QUESTION:
Sometimes, I want to quickly be able to convert miles per imperial gallon into kilometers per liter.

Create an application that will display the number of kilometers per liter (output) based on the number of miles per imperial gallon (input).

Make sure to round off the result to two decimal points. If the answer ends with a 0, it should be rounded off without the 0. So instead of 5.50, we should get 5.5.

Some useful associations relevant to this kata:
1 Imperial Gallon = 4.54609188 litres
1 Mile = 1.609344 kilometres
"""

def convert_mpg_to_kpl(mpg: float) -> float:
    """
    Converts miles per imperial gallon (mpg) to kilometers per liter (kpl).

    Parameters:
    mpg (float): The input value in miles per imperial gallon.

    Returns:
    float: The equivalent value in kilometers per liter, rounded to two decimal points.
    """
    kpl = round(mpg * 1.609344 / 4.54609188, 2)
    return float(f"{kpl:.2f}")