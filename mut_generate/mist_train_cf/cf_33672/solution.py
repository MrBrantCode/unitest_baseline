"""
QUESTION:
Write a function `count_status_letters(status: str) -> dict` that determines the number of occurrences of each letter in the status string, ignoring spaces, and returns the result as a dictionary where the keys are the letters and the values are their respective counts. The function should be case-insensitive, treating uppercase and lowercase letters as the same.

The input string `status` will have a length between 1 and 10^5 and consists of lowercase letters and may contain spaces. The function should return a dictionary where the keys are the letters present in the status string and the values are their respective counts.
"""

def count_status_letters(status: str) -> dict:
    status = status.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    letter_count = {}
    for letter in status:
        if letter.isalpha():  # Check if the character is a letter
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count