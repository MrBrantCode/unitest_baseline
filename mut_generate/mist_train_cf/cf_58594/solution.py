"""
QUESTION:
Create a function will_it_fly that takes two parameters: a list q and an integer w. The function should return True if the list q is a palindrome and the sum of its elements is less than or equal to w, otherwise it should return False. The function should return False immediately if the list q is not a palindrome.
"""

def will_it_fly(q, w):
    # Check if list q is palindrome by comparing it to its reverse.
    if q == q[::-1]:
        # If it is, check if sum of elements of q is less than or equal to w
        return sum(q) <= w
    else:
        return False