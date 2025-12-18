"""
QUESTION:
Write a function `packing_combinations(total_books)` that calculates all possible combinations of books of type A, B, and C that can be packed into a box given that a box can fit 5 books of type A, 7 books of type B, and 4 books of type C, and the total number of books to be packed is `total_books`. The function should return a list of tuples where each tuple represents the number of books of each type (Type A, Type B, Type C) respectively. Note that the order of packing does not matter.
"""

def packing_combinations(total_books):
    combinations = []
    # iterate through all possible quantities of book A up to total_books
    for books_a in range(0,total_books+1,5): 
        # iterate through all possible quantities of book B with remaining books 
        for books_b in range(0,total_books-books_a+1,7): 
            # calculate remaining books for book C 
            books_c = total_books - books_a - books_b 
            # if remainder is divisible by 4, push combination to list
            if books_c%4 == 0: 
                combinations.append((books_a,books_b,books_c))
    return combinations