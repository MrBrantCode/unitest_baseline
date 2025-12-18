"""
QUESTION:
While surfing in web I found interesting math problem called "Always perfect". That means if you add 1 to the product of four consecutive numbers the answer is ALWAYS a perfect square.
For example we have: 1,2,3,4 and the product will be 1X2X3X4=24. If we add 1 to the product that would become 25, since the result number is a perfect square the square root of 25 would be 5.

So now lets write a function which takes numbers separated by commas in string format and returns the number which is a perfect square and the square root of that number.

If string contains other characters than number or it has more or less than 4 numbers separated by comma function returns "incorrect input".

If string contains 4 numbers but not consecutive it returns "not consecutive".
"""

def check_perfect_square_from_consecutive_numbers(input_string):
    try:
        # Split the input string by commas and convert to integers
        numbers = [int(i) for i in input_string.split(',')]
        
        # Check if exactly four numbers are provided
        if len(numbers) != 4:
            return "incorrect input"
        
        # Unpack the numbers
        a, b, c, d = numbers
        
        # Check if the numbers are consecutive
        if not (a == b - 1 and a == c - 2 and a == d - 3):
            return "not consecutive"
        
        # Calculate the product of the four numbers and add 1
        product_plus_one = a * b * c * d + 1
        
        # Calculate the square root of the result
        square_root = int(product_plus_one ** 0.5)
        
        # Return the perfect square and its square root
        return product_plus_one, square_root
    
    except:
        # If any error occurs, return "incorrect input"
        return "incorrect input"