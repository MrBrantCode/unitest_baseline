"""
QUESTION:
Write a function named `calculate_ISBN` that takes four parameters: `last_name`, `book_title`, `publisher_name`, and `publication_year`. The function should return a 10-digit ISBN number generated based on the given parameters. The ISBN number is calculated by combining the first three letters of the last name, the first three letters of the book title, the first letter of the publisher's name, the last two digits of the publication year, and a checksum digit calculated using a specific algorithm. The function should handle cases where the last name or book title has less than three letters by padding with "X".
"""

def calculate_ISBN(last_name, book_title, publisher_name, publication_year):
    # Step 1: Take the first three letters of the author's last name
    author_last_name = last_name[:3].upper().ljust(3, "X")
    
    # Step 2: Take the first three letters of the book title
    book_title_short = book_title[:3].upper().ljust(3, "X")
    
    # Step 3: Take the first letter of the publisher's name
    publisher_initial = publisher_name[0].upper()
    
    # Step 4: Take the last two digits of the publication year
    year_last_two_digits = str(publication_year)[-2:]
    
    # Step 5: Concatenate all the elements
    isbn_number = author_last_name + book_title_short + publisher_initial + year_last_two_digits
    
    # Step 6: Calculate the checksum digit
    checksum = 0
    for i, char in enumerate(isbn_number):
        if char.isdigit():
            checksum += (i+1) * int(char)
    
    checksum %= 11
    if checksum == 10:
        checksum = "X"
    else:
        checksum = str(checksum)
    
    # Step 7: Append the checksum digit
    isbn_number += checksum
    
    return isbn_number