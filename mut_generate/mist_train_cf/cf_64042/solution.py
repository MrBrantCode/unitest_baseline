"""
QUESTION:
Develop a function `calculate_loan_amounts` that determines the amounts borrowed from three different loans with annual interest rates of 5%, 7%, and 9%, given a total amount of $2500 borrowed and a total interest of $200 paid after a year. The function should find all combinations of non-zero amounts that satisfy the conditions and return the amounts borrowed from each loan, ensuring the sum of these amounts equals the total borrowed amount.
"""

def calculate_loan_amounts(total_borrowed, total_interest, rate_1, rate_2, rate_3):
    """
    Calculate the amounts borrowed from three different loans.

    Args:
    total_borrowed (float): The total amount borrowed.
    total_interest (float): The total interest after a year.
    rate_1 (float): The interest rate of the first loan.
    rate_2 (float): The interest rate of the second loan.
    rate_3 (float): The interest rate of the third loan.

    Returns:
    list: A list of tuples containing the amounts borrowed for each loan.
    """
    solutions = []
    for a in range(10, total_borrowed-20, 10):
        for b in range(10, total_borrowed-a-10, 10):
            # the third loan is whatever is left over
            c = total_borrowed - a - b

            # calculate total interest
            interest = a*rate_1 + b*rate_2 + c*rate_3

            # if total interest matches specified total, add amounts to solutions
            if total_interest == interest:
                solutions.append((a, b, c))
    return solutions