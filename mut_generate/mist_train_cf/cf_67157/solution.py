"""
QUESTION:
Write a function `volume_of_tesseract(side_length)` that calculates the volume of a four-dimensional hypercube, given its side length. The volume should be calculated as `side_length` to the power of 4. The function should also include error checking to handle invalid inputs, such as negative numbers or excessively large numbers (consider numbers greater than 10^6 as excessively large). If the input is invalid, the function should return an error message.
"""

def volume_of_tesseract(side_length):
    try:
        if side_length < 0 or side_length > 10**6:
            return "Invalid input: side_length must be a non-negative number less than 10^6."

        volume = side_length ** 4
        return volume

    except TypeError:
        return "Invalid input: side_length must be a number."