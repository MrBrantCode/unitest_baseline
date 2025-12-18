"""
QUESTION:
problem

Taro bought 10 books. Later, I tried to find out the price based on the receipt, but the receipt was dirty and I could not read the price of a book. We decided to calculate the price of the book from the total price of 10 books and the prices of the other 9 books.

Write a program that outputs the price of the book whose price could not be read. The prices of books are all positive integers. Also, there is no need to consider the consumption tax.





Example

Input

9850
1050
800
420
380
600
820
2400
1800
980
0


Output

600
"""

def calculate_missing_book_price(total_price: int, known_prices: list) -> int:
    """
    Calculate the price of the book whose price was not readable from the total price of 10 books and the prices of the other 9 books.

    Parameters:
    - total_price (int): The total price of all 10 books.
    - known_prices (list): A list of the prices of the 9 books whose prices are known.

    Returns:
    - int: The price of the book whose price was not readable.
    """
    return total_price - sum(known_prices)